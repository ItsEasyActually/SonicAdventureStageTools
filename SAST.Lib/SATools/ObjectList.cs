using System.Globalization;

namespace SAST.Lib.SATools
{
	public static class ObjectList
	{
		public static ObjectListEntry[] Load(string filename, bool SA2)
		{
			if (SA2)
				return IniSerializer.Deserialize<SA2ObjectListEntry[]>(filename);
			else
				return IniSerializer.Deserialize<SA1ObjectListEntry[]>(filename);
		}
	}

	[Serializable]
	public abstract class ObjectListEntry
	{
		[IniAlwaysInclude]
		public byte Arg1 { get; set; }
		[IniAlwaysInclude]
		public byte Arg2 { get; set; }
		[IniAlwaysInclude]
		public ushort Flags { get; set; }
		public float Distance { get; set; }
		[IniIgnore]
		public uint Code { get { if (uint.TryParse(CodeString, NumberStyles.HexNumber, NumberFormatInfo.InvariantInfo, out uint code)) return code; else return uint.MaxValue; } set { CodeString = value.ToString("X8"); } }
		[IniName("Code")]
		public string CodeString { get; set; }
		public string Name { get; set; }
	}

	[Serializable]
	public class SA1ObjectListEntry : ObjectListEntry
	{
		public SA1ObjectListEntry() { CodeString = string.Empty; Name = string.Empty; }

		public int Unknown { get; set; }
	}

	[Serializable]
	public class SA2ObjectListEntry : ObjectListEntry
	{
		public SA2ObjectListEntry() { CodeString = string.Empty; Name = string.Empty; }

	}
}
