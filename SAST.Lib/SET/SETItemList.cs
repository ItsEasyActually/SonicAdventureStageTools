using System.Text.Json;
using System.Text.Json.Serialization;

namespace SAST.Lib.SET
{
	public class SETItemList
	{
		private class SETItemListINI
		{

		}

		#region Variables
		public List<string> ItemDefinitionEntries { get; set; } = new List<string>();

		[JsonIgnore]
		public List<SETItem> ItemEntries { get; set; } = new List<SETItem>();

		#endregion

		#region Constructors
		public SETItemList() { }

		#endregion

		public static SETItemList Deserialize(string path)
		{
			if (File.Exists(path))
			{
				SETItemList list = JsonSerializer.Deserialize<SETItemList>(path);
				if (list != null)
				{
					foreach (var item in list.ItemDefinitionEntries)
					{
						list.ItemEntries.Add(SETItem.Deserialize(item));
					}
					return list;
				}
			}

			return new SETItemList();
		}
	}
}
