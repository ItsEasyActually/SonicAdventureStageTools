using SAST.Lib.CAM.SA1;
using SAST.Lib.CAM.SA2;
using SAST.Lib.GameInfo;
using SAST.Lib.IO;

namespace SAST.Lib.Blender
{
	public static class ImportManager
	{
		private static T ImportFile<T>(string path) where T : IBinaryFile<T>
		{
			return T.FromFile(path);
		}

		#region SA1
		public static SA1CAMFile ImportSA1CAMFile(string path) { return ImportFile<SA1CAMFile>(path); }

		public static Dictionary<string, SA1CAMFile> ImportSA1CAMFileAuto(string directory, string levelid, string actid)
		{
			Dictionary<string, SA1CAMFile> files = new Dictionary<string, SA1CAMFile>();
			string[] names = Enum.GetNames<SA1Character>();

			for (int i = 0; i < names.Count(); i++)
			{
				string filename = SA1StageInfo.GetFilename(levelid, actid, names[i], true);
				string filepath = Path.Combine(directory, filename);
				if (File.Exists(filepath))
					files.Add(names[i], ImportSA1CAMFile(filepath));
			}

			return files;
		}

		#endregion

		#region SA2
		public static SA2CAMFile ImportSA2CAMFile(string path) 
		{ 
			SA2CAMFile file = ImportFile<SA2CAMFile>(path);
			file.SwapRotations();
			return file;
		}

		public static List<SA2CAMFile> ImportSA2CAMFileAuto(string directory, string levelid, string actid)
		{
			List<SA2CAMFile> files = new List<SA2CAMFile>();

			string filename = SA2StageInfo.GetFilename(levelid, actid, SA2ChaoRaceLevel.None.ToString(), true);
			string filepath = Path.Combine(directory, filename);
			if (File.Exists(filepath))
				files.Add(SA2CAMFile.FromFile(filepath));

			return files;
		}

		#endregion
	}
}
