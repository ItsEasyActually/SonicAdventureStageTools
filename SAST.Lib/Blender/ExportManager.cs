

using SAST.Lib.CAM.SA1;
using SAST.Lib.CAM.SA2;
using SAST.Lib.GameInfo;
using SAST.Lib.IO;
using System.Data;

namespace SAST.Lib.Blender
{
	public static class ExportManager
	{
		private static void ExportFile<T>(T item, string path, bool bigEndian) where T : IBinaryFile<T>
		{
			item.ToFile(path, bigEndian);
		}

		#region SA1
		public static void ExportSA1CamFile(SA1CAMFile file, string path, bool bigEndian) { ExportFile<SA1CAMFile>(file, path, bigEndian); }

		public static void ExportSA1CamFileAuto(Dictionary<string, SA1CAMFile> files, string directory, string stageID, string actID, bool bigEndian)
		{
			if (Directory.Exists(directory))
			{
				foreach (var file in files)
				{
					string filename = SA1StageInfo.GetFilename(stageID, actID, file.Key, true);
				
					string filepath = Path.Combine(directory, filename);

					ExportSA1CamFile(file.Value, filepath, bigEndian);
				}
			}
		}

		#endregion

		#region SA2
		public static void ExportSA2CamFile(SA2CAMFile file, string path, bool bigEndian) 
		{
			file.SwapRotationsBack();
			ExportFile<SA2CAMFile>(file, path, bigEndian);
		}

		public static void ExportSA2CamFileAuto(List<SA2CAMFile> files, string directory, string stageID, string actID, bool bigEndian)
		{
			if (Directory.Exists(directory))
			{
				foreach (var file in files)
				{
					string filename = SA2StageInfo.GetFilename(stageID, actID, "None", true);

					string filepath = Path.Combine(directory, filename);

					ExportSA2CamFile(file, filepath, bigEndian);
				}
			}
		}
		#endregion
	}
}
