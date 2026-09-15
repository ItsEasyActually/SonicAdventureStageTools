using Amicitia.IO.Binary;
using SAST.Lib.Extensions;
using SAST.Lib.IO;

namespace SAST.Lib.Specialized.SA1
{
	public class MissionParameterFile : IBinarySerializable, IBinaryFile<MissionParameterFile>
	{
		#region Variables
		private List<MissionParameterItem> MissionItems { get; set; } = new List<MissionParameterItem>();

		public int Count { get => MissionItems.Count; }

		#endregion

		#region Constructors
		public MissionParameterFile() { }

		#endregion

		#region Functions
		public void Read(BinaryObjectReader binaryReader)
		{
			long count = binaryReader.GetBaseStream().Length / MissionParameterItem.Size - 1;

			binaryReader.Seek(0x20, SeekOrigin.Begin);
			for (int i = 0; i < count; i++)
			{
				MissionItems.Add(binaryReader.ReadObject<MissionParameterItem>());
			}
		}

		public void Write(BinaryObjectWriter binaryWriter) 
		{
			binaryWriter.WriteZeroes(2);
			binaryWriter.WriteByte(0x30);
			binaryWriter.WriteByte(0x56);
			binaryWriter.WriteZeroes(0x16);

			for (int i = 0; i < MissionItems.Count; i++)
			{
				binaryWriter.WriteObject(MissionItems[i]);
			}
		}

		public void ToStream(MemoryStream stream, bool isBigEndian = false) { FileWriter.WriteStream(stream, this, isBigEndian); }

		public void ToFile(string path, bool isBigEndian = false) { FileWriter.WriteFile(path, this, isBigEndian); }

		public void AddObject(MissionParameterItem item) => MissionItems.Add(item);

		public void RemoveObject(MissionParameterItem item) => MissionItems.Remove(item);

		public void ClearObjects() => MissionItems.Clear();

		#endregion

		#region Static
		public static MissionParameterFile FromStream(MemoryStream stream) { return FileReader.ReadStream<MissionParameterFile>(stream); }

		public static MissionParameterFile FromFile(string path) { return FileReader.ReadFile<MissionParameterFile>(path); }

		#endregion
	}
}
