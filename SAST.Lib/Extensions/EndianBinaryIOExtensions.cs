using Kermalis.EndianBinaryIO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SAST.Lib.Extensions
{
	public static class EndianBinaryIOExtensions
	{
		#region EndianBinaryReader
		#region Endian Setters
		/// <summary>
		/// Sets the current <see cref="EndianBinaryReader"/> to <see cref="Endianness.LittleEndian"/>
		/// </summary>
		/// <param name="reader"></param>
		public static void SetAsLittleEndian(this EndianBinaryReader reader) { reader.Endianness = Endianness.LittleEndian; }

		/// <summary>
		/// Sets the current <see cref="EndianBinaryReader"/> to <see cref="Endianness.BigEndian"/>
		/// </summary>
		/// <param name="reader"></param>
		public static void SetAsBigEndian(this EndianBinaryReader reader) { reader.Endianness = Endianness.BigEndian; }

		#endregion

		#region Peek Extensions
		/// <summary>
		/// Returns an <see cref="int"/> at the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static int PeekInt32(this EndianBinaryReader reader)
		{
			int val = reader.ReadInt32();
			reader.Stream.Seek(-4, SeekOrigin.Current);
			return val;
		}

		/// <summary>
		/// Returns an <see cref="uint"/> as the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static uint PeekUInt32(this EndianBinaryReader reader)
		{
			uint val = reader.ReadUInt32();
			reader.Stream.Seek(-4, SeekOrigin.Current);
			return val;
		}

		/// <summary>
		/// Returns a <see cref="float"/> at the current position without advancing the position.
		/// </summary>
		/// <param name="reader"></param>
		/// <returns></returns>
		public static float PeekSingle(this EndianBinaryReader reader)
		{
			float val = reader.ReadSingle();
			reader.Stream.Seek(-4, SeekOrigin.Current);
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
		public static void CheckEndianByUInt32(this EndianBinaryReader reader)
		{
			reader.SetAsLittleEndian();
			uint little = reader.PeekUInt32();
			reader.SetAsBigEndian();
			uint big = reader.PeekUInt32();

			if (little < big)
				reader.SetAsLittleEndian();
		}

		public static void CheckEndianBySingle(this EndianBinaryReader reader)
		{
			reader.SetAsLittleEndian();
			float little = reader.PeekSingle();
			reader.SetAsBigEndian();
			float big = reader.PeekSingle();

			if (little < big)
				reader.SetAsLittleEndian();
		}

		#endregion

		#endregion

		#region EndianBinaryWriter
		#region Endian Setters
		/// <summary>
		/// Sets the <see cref="EndianBinaryWriter"/> to write in <see cref="Endianness.LittleEndian"/>
		/// </summary>
		/// <param name="writer"></param>
		public static void SetAsLittleEndian(this EndianBinaryWriter writer) { writer.Endianness = Endianness.LittleEndian; }

		/// <summary>
		/// Sets the <see cref="EndianBinaryWriter"/> to write in <see cref="Endianness.BigEndian"/>
		/// </summary>
		/// <param name="writer"></param>
		public static void SetAsBigEndian(this EndianBinaryWriter writer) { writer.Endianness = Endianness.BigEndian; }

		#endregion

		#endregion
	}
}
