using Amicitia.IO.Binary;
using SAST.Lib.DataTypes;

namespace SAST.Lib.Extensions
{
	public static class AmicitiaIOExtensions
	{
		public enum DataSize
		{
			Size8 = 0,
			Size16 = 1,
			Size32 = 2,
			Size64 = 4
		}

		#region EndianBinaryReader
		#region Endian Setters
		/// <summary>
		/// Sets the current <see cref="EndianBinaryReader"/> to <see cref="Endianness.LittleEndian"/>
		/// </summary>
		/// <param name="reader"></param>
		public static void SetAsLittleEndian(this BinaryObjectReader reader) { reader.Endianness = Endianness.Little; }

		/// <summary>
		/// Sets the current <see cref="EndianBinaryReader"/> to <see cref="Endianness.BigEndian"/>
		/// </summary>
		/// <param name="reader"></param>
		public static void SetAsBigEndian(this BinaryObjectReader reader) { reader.Endianness = Endianness.Big; }

		#endregion

		#region Peek Extensions
		/// <summary>
		/// Returns an <see cref="int"/> at the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static int PeekInt32(this BinaryObjectReader reader)
		{
			int val = reader.ReadInt32();
			reader.Seek(-4, SeekOrigin.Current);
			return val;
		}

		/// <summary>
		/// Returns an <see cref="uint"/> as the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static uint PeekUInt32(this BinaryObjectReader reader)
		{
			uint val = reader.ReadUInt32();
			reader.Seek(-4, SeekOrigin.Current);
			return val;
		}

		/// <summary>
		/// Returns a <see cref="float"/> at the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static float PeekSingle(this BinaryObjectReader reader)
		{
			float val = reader.ReadSingle();
			reader.Seek(-4, SeekOrigin.Current);
			return val;
		}

		#endregion

		#region Checkers
		/// <summary>
		/// Checks the current position's <see cref="uint"/> as <see cref="Endianness.LittleEndian"/> and <see cref="Endianness.BigEndian"/>.
		/// 
		/// Sets the reader to the correct Endianness after a comparison.
		/// </summary>
		/// <param name="reader"></param>
		public static void CheckEndianByUInt32(this BinaryObjectReader reader)
		{
			reader.SetAsLittleEndian();
			uint little = reader.PeekUInt32();
			reader.SetAsBigEndian();
			uint big = reader.PeekUInt32();

			if (little < big)
				reader.SetAsLittleEndian();
		}

		public static void CheckEndianBySingle(this BinaryObjectReader reader)
		{
			reader.SetAsLittleEndian();
			float little = reader.PeekSingle();
			reader.SetAsBigEndian();
			float big = reader.PeekSingle();

			if (little < big)
				reader.SetAsLittleEndian();
		}

		#endregion

		#region Custom Object Readers
		public static RotationVector ReadShortRotationVector(this BinaryObjectReader reader)
		{
			RotationVector rotation = new RotationVector();

			rotation.X = new Rotation(reader.ReadInt16());
			rotation.Y = new Rotation(reader.ReadInt16());
			rotation.Z = new Rotation(reader.ReadInt16());

			return rotation;
		}

		public static bool ReadBoolean(this BinaryObjectReader reader, DataSize size)
		{
			switch (size)
			{
				case DataSize.Size8:
					return (reader.ReadByte() > 0);
				case DataSize.Size16:
					return (reader.ReadInt16() > 0);
				case DataSize.Size32:
				default:
					return (reader.ReadInt32() > 0);
				case DataSize.Size64:
					return (reader.ReadInt64() > 0);
			}
		}

		public static bool ReadBooleanByte(this BinaryObjectReader reader) => reader.ReadBoolean(DataSize.Size8);

		public static bool ReadBoolean16(this BinaryObjectReader reader) => reader.ReadBoolean(DataSize.Size16);

		public static bool ReadBoolean32(this BinaryObjectReader reader) => reader.ReadBoolean(DataSize.Size32);

		public static bool ReadBoolean64(this BinaryObjectReader reader) => reader.ReadBoolean(DataSize.Size64);

		public static T ReadEnum<T>(this BinaryObjectReader reader) where T : Enum
		{
			Type enumType = Enum.GetUnderlyingType(typeof(T));
			switch (enumType.Name)
			{
				case nameof(Byte):
					return (T)(object)reader.ReadByte();
				case nameof(Int16):
					return (T)(object)reader.ReadInt16();
				case nameof(UInt16):
					return (T)(object)reader.ReadUInt16();
				case nameof(Int32):
					return (T)(object)reader.ReadInt32();
				case nameof(UInt32):
					return (T)(object)reader.ReadUInt32();
				case nameof(Int64):
					return (T)(object)reader.ReadInt64();
				case nameof(UInt64):
					return (T)(object)reader.ReadUInt64();
				default:
					return (T)(object)0;
			}
		}

		#endregion

		#endregion

		#region EndianBinaryWriter
		#region Endian Setters
		/// <summary>
		/// Sets the <see cref="EndianBinaryWriter"/> to write in <see cref="Endianness.LittleEndian"/>
		/// </summary>
		/// <param name="writer"></param>
		public static void SetAsLittleEndian(this BinaryObjectWriter writer) { writer.Endianness = Endianness.Little; }

		/// <summary>
		/// Sets the <see cref="EndianBinaryWriter"/> to write in <see cref="Endianness.BigEndian"/>
		/// </summary>
		/// <param name="writer"></param>
		public static void SetAsBigEndian(this BinaryObjectWriter writer) { writer.Endianness = Endianness.Big; }

		#endregion

		#region Custom Object Writers
		public static void WriteShortRotationVector(this BinaryObjectWriter writer, RotationVector rotation)
		{
			writer.WriteInt16(rotation.X.ToInt16());
			writer.WriteInt16(rotation.Y.ToInt16());
			writer.WriteInt16(rotation.Z.ToInt16());
		}

		public static void WriteZeroes(this BinaryObjectWriter writer, int count)
		{
			byte[] bytes = new byte[count];
			writer.WriteBytes(bytes);
		}

		public static void WriteBoolean(this BinaryObjectWriter writer, DataSize size, bool value)
		{
			int val = (value) ? 1 : 0;
			switch (size)
			{
				case DataSize.Size8:
					writer.WriteByte((byte)val);
					break;
				case DataSize.Size16:
					writer.WriteInt16((short)val);
					break;
				case DataSize.Size32:
				default:
					writer.WriteInt32(val);
					break;
				case DataSize.Size64:
					writer.WriteInt64((long)val);
					break;
			}
		}

		public static void WriteBoolean8(this BinaryObjectWriter writer, bool value) => writer.WriteBoolean(DataSize.Size8, value);

		public static void WriteBoolean16(this BinaryObjectWriter writer, bool value) => writer.WriteBoolean(DataSize.Size16, value);

		public static void WriteBoolean32(this BinaryObjectWriter writer, bool value) => writer.WriteBoolean(DataSize.Size32, value);

		public static void WriteBoolean64(this BinaryObjectWriter writer, bool value) => writer.WriteBoolean(DataSize.Size64, value);

		public static void WriteEnum<T>(this BinaryObjectWriter writer, T value) where T : Enum
		{
			Type enumType = Enum.GetUnderlyingType(typeof(T));
			switch (enumType.Name)
			{
				case nameof(Byte):
					writer.WriteByte((byte)(object)value);
					break;
				case nameof(Int16):
					writer.WriteInt16((short)(object)value);
					break;
				case nameof(UInt16):
					writer.WriteUInt16((ushort)(object)value);
					break;
				case nameof(Int32):
				default:
					writer.WriteInt32((int)(object)value);
					break;
				case nameof(UInt32):
					writer.WriteUInt32((uint)(object)value);
					break;
				case nameof(Int64):
					writer.WriteInt64((long)(object)value);
					break;
				case nameof(UInt64):
					writer.WriteUInt64((ulong)(object)value);
					break;
			}
		}

		#endregion

		#endregion
	}
}
