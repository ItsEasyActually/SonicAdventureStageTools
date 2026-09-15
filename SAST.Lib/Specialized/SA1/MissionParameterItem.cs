using Amicitia.IO.Binary;
using SAST.Lib.Extensions;

namespace SAST.Lib.Specialized.SA1
{
	public class MissionParameterItem : IBinarySerializable
	{
		public enum MissionIndex : byte
		{
			Mission1 = 0,
			Mission2 = 1,
			Mission3 = 2,
			Mission4 = 3,
			Mission5 = 4,
			Mission6 = 5,
			Mission7 = 6,
			Mission8 = 7,
			Mission9 = 8,
			Mission10 = 9,
			Mission11 = 10,
			Mission12 = 11,
			Mission13 = 12,
			Mission14 = 13,
			Mission15 = 14,
			Mission16 = 15,
			Mission17 = 16,
			Mission18 = 17,
			Mission19 = 18,
			Mission20 = 19,
			Mission21 = 20,
			Mission22 = 21,
			Mission23 = 22,
			Mission24 = 23,
			Mission25 = 24,
			Mission26 = 25,
			Mission27 = 26,
			Mission28 = 27,
			Mission29 = 28,
			Mission30 = 29,
			Mission31 = 30,
			Mission32 = 31,
			Mission33 = 32,
			Mission34 = 33,
			Mission35 = 34,
			Mission36 = 35,
			Mission37 = 36,
			Mission38 = 37,
			Mission39 = 38,
			Mission40 = 39,
			Mission41 = 40,
			Mission42 = 41,
			Mission43 = 42,
			Mission44 = 43,
			Mission45 = 44,
			Mission46 = 45,
			Mission47 = 46,
			Mission48 = 47,
			Mission49 = 48,
			Mission50 = 49,
			Mission51 = 50,
			Mission52 = 51,
			Mission53 = 52,
			Mission54 = 53,
			Mission55 = 54,
			Mission56 = 55,
			Mission57 = 56,
			Mission58 = 57,
			Mission59 = 58,
			Mission60 = 59
		}

		public enum MissionDisplayFlag : byte
		{
			BeforeMission = 0,
			DuringMission = 1,
			DuringTimer = 5
		}

		public enum MissionItemType : byte
		{
			LevelObjectList = 0,
			MissionObjectList = 1
		}

		#region Variables
		/// <summary>
		/// <see cref="MissionIndex"/> that the object belongs to.
		/// </summary>
		public MissionIndex MissionID { get; set; } = MissionIndex.Mission1;

		/// <summary>
		/// <see cref="MissionDisplayFlag"/> flag that sets when the object should be visible.
		/// </summary>
		public MissionDisplayFlag DisplayFlag { get; set; } = MissionDisplayFlag.DuringMission;

		/// <summary>
		/// <see cref="MissionItemType"/> defines which Object List the object is sourced from.
		/// </summary>
		public MissionItemType ObjectList { get; set; } = MissionItemType.MissionObjectList;

		/// <summary>
		/// A value to set the timer if an object uses a timer setup.
		/// </summary>
		public byte Timer { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0000 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0001 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0002 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0003 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0100 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0101 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0102 { get; set; } = 0;

		/// <summary>
		/// Part of a union, read as a byte in-game.
		/// </summary>
		public byte Param0103 { get; set; } = 0;

		#endregion

		public MissionParameterItem() { }

		#region Functions
		public void Read(BinaryObjectReader binaryReader)
		{
			MissionID = binaryReader.ReadEnum<MissionIndex>();
			DisplayFlag = binaryReader.ReadEnum<MissionDisplayFlag>();
			ObjectList = binaryReader.ReadEnum<MissionItemType>();
			Timer = binaryReader.ReadByte();

			Param0000 = binaryReader.ReadByte();
			Param0001 = binaryReader.ReadByte();
			Param0002 = binaryReader.ReadByte();
			Param0003 = binaryReader.ReadByte();
			
			Param0100 = binaryReader.ReadByte();
			Param0101 = binaryReader.ReadByte();
			Param0102 = binaryReader.ReadByte();
			Param0103 = binaryReader.ReadByte();

		}

		public void Write(BinaryObjectWriter binaryWriter)
		{
			binaryWriter.WriteEnum(MissionID);
			binaryWriter.WriteEnum(DisplayFlag);
			binaryWriter.WriteEnum(ObjectList);
			binaryWriter.WriteByte(Timer);

			binaryWriter.WriteByte(Param0000);
			binaryWriter.WriteByte(Param0001);
			binaryWriter.WriteByte(Param0002);
			binaryWriter.WriteByte(Param0003);

			binaryWriter.WriteByte(Param0100);
			binaryWriter.WriteByte(Param0101);
			binaryWriter.WriteByte(Param0102);
			binaryWriter.WriteByte(Param0103);
		}

		#endregion

		#region Static
		public static readonly int Size = 0xC;

		#endregion 
	}
}
