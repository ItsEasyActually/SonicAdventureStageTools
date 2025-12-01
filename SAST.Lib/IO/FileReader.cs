using AuroraLib.Compression.Algorithms;
using Kermalis.EndianBinaryIO;
using SAST.Lib.Extensions;
using System.IO;

namespace SAST.Lib.IO
{
	/// <summary>
	/// File Reading helper class, mostly exists to reduce code being written in file reading applications.
	/// </summary>
	public static class FileReader
	{
		/// <summary>
		/// Returns an object of T from the provided <see cref="MemoryStream"/>
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="stream">Current stream for the file.</param>
		/// <returns></returns>
		public static T ReadStream<T>(MemoryStream stream)
		{
			EndianBinaryReader reader = new EndianBinaryReader(stream);
			reader.Stream.Seek(0, SeekOrigin.Begin);

			return reader.ReadObject<T>();
		}

		/// <summary>
		/// Returns an object of T from the provided file path.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="path">Path to the file.</param>
		/// <returns></returns>
		public static T ReadFile<T>(string path)
		{
			string filepath = Path.GetFullPath(path);

			if (File.Exists(filepath))
			{
				using (MemoryStream stream = new MemoryStream(File.ReadAllBytes(filepath)))
				{
					return ReadStream<T>(stream);
				}
			}
			else
				return default;
		}

		/// <summary>
		/// Returns an object of T from a PRS Compressed file from the provided file path.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="path"></param>
		/// <returns></returns>
		public static T ReadCompressedFile<T>(string path)
		{
			string filepath = Path.GetFullPath(path);

			if (File.Exists(filepath))
			{
				using (MemoryStream deststream = new MemoryStream())
				{
					using (MemoryStream sourcestream = new MemoryStream(File.ReadAllBytes(filepath)))
					{
						PRS.DecompressHeaderless(sourcestream, deststream);
					}
					return ReadStream<T>(deststream);
				}
			}
			else
				return default;
		}
	}
}
