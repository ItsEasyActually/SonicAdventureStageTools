using Amicitia.IO.Streams;
using Amicitia.IO.Binary;
using SA3D.Archival;

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
		public static T ReadStream<T>(MemoryStream stream) where T : IBinarySerializable, new()
		{
			using BinaryObjectReader reader = new BinaryObjectReader(stream, StreamOwnership.Retain, Endianness.Little);

			return reader.ReadObject<T>();
		}

		/// <summary>
		/// Returns an object of T from the provided file path.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="path">Path to the file.</param>
		/// <returns></returns>
		public static T ReadFile<T>(string path) where T : IBinarySerializable, new()
		{
			string filepath = Path.GetFullPath(path);

			if (File.Exists(filepath))
			{
				using BinaryObjectReader reader = new BinaryObjectReader(filepath, Endianness.Little, null);
				
				return reader.ReadObject<T>();
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
		public static T ReadCompressedFile<T>(string path) where T : IBinarySerializable, new()
		{
			string filepath = Path.GetFullPath(path);

			if (File.Exists(filepath))
			{
				using (MemoryStream deststream = new MemoryStream(PRS.ReadPRSFile(filepath)))
				{
					return ReadStream<T>(deststream);
				}
			}
			else
				return default;
		}
	}
}
