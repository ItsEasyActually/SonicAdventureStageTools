using Kermalis.EndianBinaryIO;
using SAST.Lib.Extensions;
using SAST.Lib.IO;

namespace SAST.Lib.SET
{
	public class SETFile : IBinarySerializable, IBinaryFile<SETFile>
	{
		#region Variables
		/// <summary>
		/// List of <see cref="SETObject"/>.
		/// </summary>
		protected List<SETObject> Objects = new List<SETObject>();

		/// <summary>
		/// Total number of <see cref="SETObject"/>s in the <see cref="SETFile"/>.
		/// </summary>
		public int ObjectCount { get { return Objects.Count; } }

		/// <summary>
		/// Adds a <see cref="SETObject"/> to the <see cref="SETFile"/>'s Cameras.
		/// </summary>
		/// <param name="obj"></param>
		public void AddObject(SETObject obj) { Objects.Add(obj); }

		/// <summary>
		/// Removes the supplied <see cref="SETObject"/> from the <see cref="SETFile"/>'s Cameras.
		/// </summary>
		/// <param name="obj"></param>
		public void RemoveObject(SETObject obj) { Objects.Remove(obj); }

		/// <summary>
		/// Removes the <see cref="SETObject"/> at the supplied index from the <see cref="SETFile"/>'s Cameras.
		/// </summary>
		/// <param name="index"></param>
		public void RemoveObject(int index) { Objects.RemoveAt(index); }

		/// <summary>
		/// Clears the <see cref="SETFile"/>'s Cameras.
		/// </summary>
		public void ClearObjects() { Objects.Clear(); }

		/// <summary>
		/// Gets the <see cref="SETFile"/>'s Cameras.
		/// </summary>
		/// <returns>A copy of the Cameras List.</returns>
		public List<SETObject> GetObjects() { return Objects; }

		#endregion

		#region Constructors
		public SETFile() { }

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SETFile"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			endianBinaryReader.CheckEndianByUInt32();
			int count = endianBinaryReader.ReadInt32();
			endianBinaryReader.Stream.Seek(28, SeekOrigin.Current);

			for (int i = 0; i < count; i++)
				AddObject(endianBinaryReader.ReadObject<SETObject>());
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SETFile"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteInt32(Objects.Count);
			endianBinaryWriter.WriteZeroes(28);

			foreach (SETObject obj in Objects)
				endianBinaryWriter.WriteObject(obj);
		}

		public void ToStream(MemoryStream stream, bool isBigEndian = false) { FileWriter.WriteStream(stream, this, isBigEndian); }

		public void ToFile(string path, bool isBigEndian = false) { FileWriter.WriteFile(path, this, isBigEndian); }

		#endregion

		#region Static
		public static SETFile FromStream(MemoryStream stream) { return FileReader.ReadStream<SETFile>(stream); }

		public static SETFile FromFile(string path) { return FileReader.ReadFile<SETFile>(path); }

		#endregion
	}
}
