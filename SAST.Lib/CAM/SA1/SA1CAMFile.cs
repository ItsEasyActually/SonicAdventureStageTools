using Kermalis.EndianBinaryIO;
using SAST.Lib.Extensions;
using SAST.Lib.IO;

namespace SAST.Lib.CAM.SA1
{
	public class SA1CAMFile : IBinarySerializable, IBinaryFile<SA1CAMFile>
	{
		#region Internal
		#region Variables
		/// <summary>
		/// List of <see cref="SA1CamObject"/>.
		/// </summary>
		protected List<SA1CAMObject> Cameras = new List<SA1CAMObject>();

		/// <summary>
		/// Total number of <see cref="SA1CamObject"/>s in the <see cref="SA1CamFile"/>.
		/// </summary>
		public int CameraCount { get { return Cameras.Count; } }

		/// <summary>
		/// Adds a <see cref="SA1CamObject"/> to the <see cref="SA1CamFile"/>'s Cameras.
		/// </summary>
		/// <param name="camera"></param>
		public void AddCamera(SA1CAMObject camera) { Cameras.Add(camera); }

		/// <summary>
		/// Removes the supplied <see cref="SA1CamObject"/> from the <see cref="SA1CamFile"/>'s Cameras.
		/// </summary>
		/// <param name="camera"></param>
		public void RemoveCamera(SA1CAMObject camera) { Cameras.Remove(camera); }

		/// <summary>
		/// Removes the <see cref="SA1CamObject"/> at the supplied index from the <see cref="SA1CamFile"/>'s Cameras.
		/// </summary>
		/// <param name="index"></param>
		public void RemoveCamera(int index) { Cameras.RemoveAt(index); }

		/// <summary>
		/// Clears the <see cref="SA1CamFile"/>'s Cameras.
		/// </summary>
		public void ClearCameras() { Cameras.Clear(); }

		/// <summary>
		/// Gets the <see cref="SA1CamFile"/>'s Cameras.
		/// </summary>
		/// <returns>A copy of the Cameras List.</returns>
		public List<SA1CAMObject> GetCameras() { return Cameras; }

		#endregion

		#region Constructors
		/// <summary>
		/// Default constructor.
		/// </summary>
		public SA1CAMFile() { }

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SA1CamFile"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			endianBinaryReader.CheckEndianByUInt32();
			int count = endianBinaryReader.ReadInt32();
			endianBinaryReader.Stream.Seek(60, SeekOrigin.Current);

			for (int i = 0; i < count; i++)
				AddCamera(endianBinaryReader.ReadObject<SA1CAMObject>());
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SA1CamFile"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteInt32(CameraCount);
			endianBinaryWriter.WriteZeroes(60);

			foreach (SA1CAMObject obj in Cameras)
				endianBinaryWriter.WriteObject(obj);
		}

		public void ToStream(MemoryStream stream, bool isBigEndian = false)
		{
			EndianBinaryWriter writer = new EndianBinaryWriter(stream);

			if (isBigEndian)
				writer.SetAsBigEndian();

			writer.WriteObject(this);
		}

		public void ToFile(string path, bool isBigEndian = false)
		{
			if (CameraCount > 0)
				FileWriter.WriteFile(path, this, isBigEndian);
			else
				Console.WriteLine("SA1CamFile has no Objects. Nothing to save!");
		}

		#endregion
		#endregion

		#region Static
		public static SA1CAMFile FromStream(MemoryStream stream) { return FileReader.ReadStream<SA1CAMFile>(stream); }

		public static SA1CAMFile FromFile(string path) { return FileReader.ReadFile<SA1CAMFile>(path); }

		#endregion
	}
}
