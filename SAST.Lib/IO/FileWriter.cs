using Amicitia.IO.Binary;
using Amicitia.IO.Streams;
using SA3D.Archival;

namespace SAST.Lib.IO
{
	/// <summary>
	/// 
	/// </summary>
	public static class FileWriter
	{
		/// <summary>
		/// 
		/// </summary>
		/// <param name="stream"></param>
		public static void WriteStream<T>(MemoryStream stream, T writeObject, bool isBigEndian = false) where T : IBinarySerializable, new()
		{
			using BinaryObjectWriter writer = new BinaryObjectWriter(stream, StreamOwnership.Retain, Endianness.Little);
			//writer.Stream.Seek(0, SeekOrigin.Begin);

			if (isBigEndian)
				writer.Endianness = Endianness.Big;

			writer.WriteObject(writeObject);
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="path"></param>
		public static void WriteFile<T>(string path, T writeObject, bool isBigEndian = false) where T : IBinarySerializable, new()
		{
			string filepath = Path.GetFullPath(path);

			using (MemoryStream stream = new MemoryStream())
			{
				WriteStream(stream, writeObject, isBigEndian);

				File.WriteAllBytes(filepath, stream.ToArray());
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="path"></param>
		public static void WriteCompressedFile<T>(string path, T writeObject, bool isBigEndian = false) where T : IBinarySerializable, new()
		{
			string filepath = Path.GetFullPath(path);

			using (MemoryStream stream = new MemoryStream())
			{
				WriteStream(stream, writeObject, isBigEndian);

				File.WriteAllBytes(filepath, PRS.Compress(stream.ToArray()));
			}
		}
	}
}
