using Kermalis.EndianBinaryIO;

namespace SAST.Lib.DataTypes
{
	/// <summary>
	/// A <see cref="Vector{T}"/> comprised of floats to represent a point in 3D space.
	/// </summary>
	public class FloatVector : Vector<float>, IBinarySerializable
	{
		#region Internal
		#region Constructors
		/// <summary>
		/// Creates a new <see cref="FloatVector"/> with default values of 0.0f.
		/// </summary>
		public FloatVector()
		{
			X = 0; Y = 0; Z = 0;
		}

		/// <summary>
		/// Creates a new <see cref="FloatVector"/> from the supplied x, y, and z float values.
		/// </summary>
		/// <param name="x"></param>
		/// <param name="y"></param>
		/// <param name="z"></param>
		public FloatVector(float x, float y, float z)
		{
			X = x;
			Y = y;
			Z = z;
		}

		#endregion

		#region Functions
		/// <summary>
		/// Multiplies the <see cref="FloatVector"/> with the supplied <see cref="FloatVector"/>.
		/// 
		/// Operation is in X * X, Y * Y, and Z * Z order.
		/// </summary>
		/// <param name="scalar"><see cref="FloatVector"/> to multiply by.</param>
		public void MultiplyVector(float scalar)
		{
			X *= scalar;
			Y *= scalar;
			Z *= scalar;
		}

		/// <summary>
		/// Multiplies the <see cref="float"/> with the supplied x, y, and z values.
		/// 
		/// Operation is in X * X, Y * Y, and Z * Z order.
		/// </summary>
		/// <param name="xscalar">X value to multiply by.</param>
		/// <param name="yscalar">Y value to multiply by.</param>
		/// <param name="zscalar">Z value to multiply by.</param>
		public void MultiplyVector(float xscalar, float yscalar, float zscalar)
		{
			X *= xscalar;
			Y *= yscalar;
			Z *= zscalar;
		}

		/// <summary>
		/// Checks if the <see cref="FloatVector"/> is equal to a FloatVector of 0,0,0.
		/// </summary>
		/// <returns>True if X, Y, and Z are equal to 0.0f, else returns False.</returns>
		public bool IsEmpty()
		{
			if (X == 0.0f && Y == 0.0f && Z == 0.0f)
				return true;
			else
				return false;
		}

		/// <summary>
		/// Swaps Y and Z axis for orienting into Blender.
		/// </summary>
		/// <param name="noNegate"></param>
		public void SwapOrientation(bool noNegate = false)
		{
			float y = Y;
			float z = Z;

			if (noNegate)
			{
				Y = z;
				Z = y;
			}
			else
			{
				Y = -z;
				Z = y;
			}
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="FloatVector"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			X = endianBinaryReader.ReadSingle();
			Y = endianBinaryReader.ReadSingle();
			Z = endianBinaryReader.ReadSingle();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="FloatVector"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteSingle(X);
			endianBinaryWriter.WriteSingle(Y);
			endianBinaryWriter.WriteSingle(Z);
		}

		#endregion
		#endregion

		#region Static
		#region Defaults
		public static FloatVector Zero = new FloatVector(0.0f, 0.0f, 0.0f);

		public static FloatVector Up = new FloatVector(0.0f, 1.0f, 0.0f);

		public static FloatVector Down = new FloatVector(0.0f, -1.0f, 0.0f);

		#endregion

		#region Functions
		/// <summary>
		/// Calculates the Dot 
		/// </summary>
		/// <param name="a"></param>
		/// <param name="b"></param>
		/// <returns></returns>
		public static float Dot(FloatVector a, FloatVector b)
		{
			return (a.X * b.X) + (a.Y * b.Y) + (a.Z * b.Z);
		}

		#endregion
		#endregion
	}
}
