using Kermalis.EndianBinaryIO;
using AuroraLib.Compression.Algorithms;
using SAST.Lib.Extensions;

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
		public static void WriteStream(MemoryStream stream, object writeObject, bool isBigEndian = false)
		{
			EndianBinaryWriter writer = new EndianBinaryWriter(stream);
			//writer.Stream.Seek(0, SeekOrigin.Begin);

			if (isBigEndian)
				writer.SetAsBigEndian();

			writer.WriteObject(writeObject);
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="path"></param>
		public static void WriteFile(string path, object writeObject, bool isBigEndian = false)
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
		public static void WriteCompressedFile(string path, object writeObject, bool isBigEndian = false)
		{
			string filepath = Path.GetFullPath(path);

			using (MemoryStream stream = new MemoryStream())
			{
				WriteStream(stream, writeObject, isBigEndian);
				using (MemoryStream compressedStream = new MemoryStream())
				{
					PRS.CompressHeaderless(stream.ToArray(), compressedStream);
					File.WriteAllBytes(filepath, compressedStream.ToArray());
				}
			}
		}
	}
}
