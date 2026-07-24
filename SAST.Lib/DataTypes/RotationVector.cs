using Amicitia.IO.Binary;
using System.Numerics;

namespace SAST.Lib.DataTypes
{
	public class RotationVector : Vector<Rotation>, IBinarySerializable
	{
		public enum AxisOrder
		{
			XYZ,
			XZY,
			YXZ,
			YZX,
			ZXY,
			ZYX,
		}

		#region Internal
		#region Constructors
		/// <summary>
		/// Defaults a new RotationVector is 0 as the <see cref="Rotation.Angle"/> for the X, Y, and Z axis.
		/// </summary>
		public RotationVector()
		{
			X = new Rotation();
			Y = new Rotation();
			Z = new Rotation();
		}

		/// <summary>
		/// Creates a new <see cref="RotationVector"/> using the supplied x, y, and z values.
		/// </summary>
		/// <param name="x">X Axis Angle in BAMS</param>
		/// <param name="y">Y Axis Angle in BAMS</param>
		/// <param name="z">Z Axis Angle in BAMS</param>
		public RotationVector(int x, int y, int z)
		{
			X = new Rotation(x);
			Y = new Rotation(y);
			Z = new Rotation(z);
		}

		/// <summary>
		/// Creates a new <see cref="RotationVector"/> using the supplied x, y, and z values.
		/// </summary>
		/// <param name="x">X Axis Angle in Short BAMS</param>
		/// <param name="y">Y Axis Angle in Short BAMS</param>
		/// <param name="z">Z Axis Angle in Short BAMS</param>
		public RotationVector(ushort x, ushort y, ushort z)
		{
			X = new Rotation(x);
			Y = new Rotation(y);
			Z = new Rotation(z);
		}

		#endregion

		#region Functions
		/// <summary>
		/// Converts the <see cref="RotationVector"/> to a <see cref="Quaternion"/> using the specified <see cref="AxisOrder"/>
		/// 
		/// Ported from Blender's mathutils module.
		/// </summary>
		/// <param name="order">The order the rotations are applied.</param>
		/// <returns>A <see cref="Quaternion"/></returns>
		public Quaternion ToQuaterion(AxisOrder order = AxisOrder.XYZ)
		{
			List<float> euler = new List<float>() { X.Radians, Y.Radians, Z.Radians };
			int i, j, k;
			bool parity = false;

			switch (order)
			{
				default:
				case AxisOrder.XYZ:
					i = 0;
					j = 1;
					k = 2;
					break;
				case AxisOrder.XZY:
					i = 0;
					j = 2;
					k = 1;
					parity = true;
					break;
				case AxisOrder.YXZ:
					i = 1;
					j = 0;
					k = 2;
					parity = true;
					break;
				case AxisOrder.YZX:
					i = 1;
					j = 2;
					k = 0;
					break;
				case AxisOrder.ZXY:
					i = 2;
					j = 0;
					k = 1;
					break;
				case AxisOrder.ZYX:
					i = 2;
					j = 1;
					k = 0;
					parity = true;
					break;
			}

			float ti, tj, th;

			ti = euler[i] * 0.5f;
			tj = euler[j] * (parity ? -0.5f : 0.5f);
			th = euler[k] * 0.5f;

			float ci = MathF.Cos(ti);
			float cj = MathF.Cos(tj);
			float ch = MathF.Cos(th);
			float si = MathF.Sin(ti);
			float sj = MathF.Sin(tj);
			float sh = MathF.Sin(th);

			float cc = ci * ch;
			float cs = ci * sh;
			float sc = si * ch;
			float ss = si * sh;

			List<float> a = new List<float>() { 0.0f, 0.0f, 0.0f };

			a[i] = cj * sc - sj * cs;
			a[j] = cj * ss + sj * cc;
			a[k] = cj * cs - sj * sc;

			List<float> q = new List<float>(4) { 0.0f, 0.0f, 0.0f, 0.0f };

			q[0] = cj * cc + sj * ss;
			q[1] = a[0];
			q[2] = a[1];
			q[3] = a[2];

			if (parity)
				q[j + 1] = -q[j + 1];

			return new Quaternion(q[1], q[2], q[3], q[0]);
		}

		/// <summary>
		/// Converts the <see cref="RotationVector"/> to a <see cref="Matrix4x4"/> using the specified <see cref="AxisOrder"/>.
		/// </summary>
		/// <param name="order"></param>
		/// <returns>A <see cref="Matrix4x4"/></returns>
		public Matrix4x4 ToMatrix4(AxisOrder order = AxisOrder.XYZ)
		{
			return Matrix4x4.CreateFromQuaternion(ToQuaterion(order));
		}

		/// <summary>
		/// Computes the Euler Angle in the specified <see cref="AxisOrder"/> from the supplied <see cref="Quaternion"/>
		/// </summary>
		/// <param name="q">A normalized <see cref="Quaternion"/></param>
		/// <param name="order">The order the rotations are applied.</param>
		private void ComputeEulerFromQuaternion(Quaternion q, AxisOrder order)
		{
			// Source ported from https://github.com/evbernardes/quaternion_to_euler, modified to fit the needs of this library.
			// Credit to Evandro Bernardes for the original module.

			List<float> quat = new List<float>() { q.X, q.Y, q.Z, q.W };
			int i, j, k, sign;

			switch (order)
			{
				default:
				case AxisOrder.XYZ:
					i = 0;
					j = 1;
					k = 2;
					break;
				case AxisOrder.XZY:
					i = 0;
					j = 2;
					k = 1;
					break;
				case AxisOrder.YXZ:
					i = 1;
					j = 0;
					k = 2;
					break;
				case AxisOrder.YZX:
					i = 1;
					j = 2;
					k = 0;
					break;
				case AxisOrder.ZXY:
					i = 2;
					j = 0;
					k = 1;
					break;
				case AxisOrder.ZYX:
					i = 2;
					j = 1;
					k = 0;
					break;
			}

			sign = (i - j) * (j - k) * (k - i) / 2;

			float a = quat[3] - quat[j];
			float b = quat[i] + quat[k] * sign;
			float c = quat[j] + quat[3];
			float d = quat[k] * sign - quat[i];

			float lengthsq = a * a + b * b + c * c + d * d;

			List<float> angles = new List<float>() { 0.0f, 0.0f, 0.0f };

			angles[1] = MathF.Acos(2 * (a * a + b * b) / lengthsq - 1);

			bool safe1 = MathF.Abs(angles[1]) >= float.Epsilon;
			bool safe2 = MathF.Abs(angles[1] - MathF.PI) >= float.Epsilon;
			bool safe = safe1 & safe2;
			float half_sum, half_diff;

			if (safe)
			{
				half_sum = MathF.Atan2(b, a);
				half_diff = MathF.Atan2(-d, c);

				angles[0] = half_sum + half_diff;
				angles[2] = half_sum - half_diff;
			}
			else
			{
				if (!safe)
				{
					angles[0] = 0;
				}

				if (!safe1)
				{
					half_sum = MathF.Atan2(b, a);
					angles[2] = 2 * half_sum;
				}

				if (!safe2)
				{
					half_diff = MathF.Atan2(-d, c);
					angles[2] = -2 * half_diff;
				}
			}

			for (int i_ = 0; i_ < 3; i_++)
			{
				if (angles[i_] < -Math.PI)
					angles[i_] += 2 * MathF.PI;
				else if (angles[i_] > MathF.PI)
					angles[i_] -= 2 * MathF.PI;
			}

			angles[2] *= sign;
			angles[1] -= MathF.PI / 2;

			if (order == AxisOrder.YZX)
			{
				X = Rotation.CreateRotationFromRadians(angles[j]);
				Y = Rotation.CreateRotationFromRadians(angles[k]);
				Z = Rotation.CreateRotationFromRadians(angles[i]);
			}
			else if (order == AxisOrder.ZXY)
			{
				X = Rotation.CreateRotationFromRadians(angles[k]);
				Y = Rotation.CreateRotationFromRadians(angles[i]);
				Z = Rotation.CreateRotationFromRadians(angles[j]);
			}
			else
			{
				X = Rotation.CreateRotationFromRadians(angles[i]);
				Y = Rotation.CreateRotationFromRadians(angles[j]);
				Z = Rotation.CreateRotationFromRadians(angles[k]);
			}
		}

		/// <summary>
		/// Converts a <see cref="Quaternion"/> into a <see cref="RotationVector"/> using the specified <see cref="AxisOrder"/>.
		/// </summary>
		/// <param name="q">A normalized <see cref="Quaternion"/></param>
		/// <param name="order">The order the rotations are applied.</param>
		public void FromQuaternion(Quaternion q, AxisOrder order = AxisOrder.XYZ)
		{
			ComputeEulerFromQuaternion(Quaternion.Normalize(q), order);
		}

		/// <summary>
		/// Swaps a <see cref="RotationVector"/>'s rotation order with another using a <see cref="Quaternion"/>.
		/// </summary>
		/// <param name="inOrder">Input order of the rotations.</param>
		/// <param name="outOrder">Output order of the rotations.</param>
		public void SwapAxisOrder(AxisOrder inOrder, AxisOrder outOrder)
		{
			FromQuaternion(ToQuaterion(inOrder), outOrder);
		}

		/// <summary>
		/// Returns a <see cref="FloatVector"/> for Euler Rotations as degrees or radians. Allows swapping axis order.
		/// </summary>
		/// <param name="radians">Returns values as radians when true, otherwise returns degrees.</param>
		/// <param name="inOrder"></param>
		/// <param name="outOrder"></param>
		/// <returns></returns>
		public FloatVector GetEulerRotations(bool radians = false, AxisOrder inOrder = AxisOrder.XYZ, AxisOrder outOrder = AxisOrder.XYZ)
		{
			RotationVector temp = this;

			if (inOrder != outOrder)
				temp.SwapAxisOrder(inOrder, outOrder);

			if (radians)
				return new FloatVector(temp.X.Radians, temp.Y.Radians, temp.Z.Radians);
			else
				return new FloatVector(temp.X.Degrees, temp.Y.Degrees, temp.Z.Degrees);
		}

		/// <summary>
		/// Swaps Y and Z axis for orienting into Blender.
		/// </summary>
		/// <param name="noNegate"></param>
		public void SwapOrientation(bool noNegate = false)
		{
			float y = Y.Degrees;
			float z = Z.Degrees;

			if (noNegate)
			{
				Z.FromDegrees(y);
				Y.FromDegrees(z);
			}
			else
			{
				Z.FromDegrees(-y);
				Y.FromDegrees(z);
			}
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="RotationVector"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(BinaryObjectReader endianBinaryReader)
		{
			X = endianBinaryReader.ReadObject<Rotation>();
			Y = endianBinaryReader.ReadObject<Rotation>();
			Z = endianBinaryReader.ReadObject<Rotation>();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="RotationVector"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(BinaryObjectWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteObject(X);
			endianBinaryWriter.WriteObject(Y);
			endianBinaryWriter.WriteObject(Z);
		}

		#endregion

		#endregion

		#region Static
		#region Creation
		/// <summary>
		/// Creates a new <see cref="RotationVector"/> from the supplied Degree angles.
		/// </summary>
		/// <param name="x">X Angle in Degrees</param>
		/// <param name="y">Y Angle in Degrees</param>
		/// <param name="z">Z Angle in Degrees</param>
		/// <returns></returns>
		static public RotationVector CreateFromEulerDegrees(float x, float y, float z)
		{
			RotationVector rVec = new RotationVector();

			rVec.X = Rotation.CreateRotationFromDegrees(x);
			rVec.Y = Rotation.CreateRotationFromDegrees(y);
			rVec.Z = Rotation.CreateRotationFromDegrees(z);

			return rVec;
		}

		/// <summary>
		/// Creates a new <see cref="RotationVector"/> from the supplied Radian angles.
		/// </summary>
		/// <param name="x">X Angle in Radians</param>
		/// <param name="y">Y Angle in Radians</param>
		/// <param name="z">Z Angle in Radians</param>
		/// <returns></returns>
		static public RotationVector CreateFromEulerRadians(float x, float y, float z)
		{
			RotationVector rVec = new RotationVector();

			rVec.X = Rotation.CreateRotationFromRadians(x);
			rVec.Y = Rotation.CreateRotationFromDegrees(y);
			rVec.Z = Rotation.CreateRotationFromRadians(z);

			return rVec;
		}

		/// <summary>
		/// Creates a new <see cref="RotationVector"/> from the supplied <see cref="Quaternion"/> and <see cref="AxisOrder"/>
		/// </summary>
		/// <param name="q">A quaternion</param>
		/// <param name="order"></param>
		/// <returns></returns>
		static public RotationVector CreateFromQuaternion(Quaternion q, AxisOrder order = AxisOrder.XYZ)
		{
			RotationVector r = new RotationVector();
			r.FromQuaternion(q, order);
			return r;
		}

		#endregion

		#endregion
	}
}
