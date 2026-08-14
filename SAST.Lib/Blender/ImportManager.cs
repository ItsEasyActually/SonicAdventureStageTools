using SAST.Lib.CAM.SA1;
using SAST.Lib.CAM.SA2;
using SAST.Lib.GameInfo;
using SAST.Lib.IO;
using SAST.Lib.SET;

namespace SAST.Lib.Blender
{
	public static class ImportManager
	{
		/// <summary>
		/// Imports a file of <typeparamref name="T"/> 
		/// </summary>
		/// <typeparam name="T"><see cref="IBinaryFile{T}"/></typeparam>
		/// <param name="path">Filepath</param>
		/// <returns></returns>
		private static T ImportFile<T>(string path) where T : IBinaryFile<T>
		{
			return T.FromFile(path);
		}

		#region Manual Import
		/// <summary>
		/// Imports a <see cref="SETFile"/>.
		/// </summary>
		/// <param name="path"></param>
		/// <returns></returns>
		public static SETFile ImportSETFile(string path) { return ImportFile<SETFile>(path); }

		/// <summary>
		/// Imports a <see cref="SA1CAMFile"/>.
		/// </summary>
		/// <param name="path"></param>
		/// <returns></returns>
		public static SA1CAMFile ImportSA1CAMFile(string path) { return ImportFile<SA1CAMFile>(path); }

		/// <summary>
		/// Imports a <see cref="SA2CAMFile"/>
		/// </summary>
		/// <param name="path"></param>
		/// <returns></returns>
		public static SA2CAMFile ImportSA2CAMFile(string path)
		{
			SA2CAMFile file = ImportFile<SA2CAMFile>(path);
			file.SwapRotations();
			return file;
		}

		#endregion

		#region Automatic Import
		/// <summary>
		/// Automatic SA1 File imports using a Directory, Level ID, and Act ID.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		private static Dictionary<string, T> ImportSA1File<T>(string directory, string levelid, string actid, bool isCamFile) where T : IBinaryFile<T>
		{
			Dictionary<string, T> files = new Dictionary<string, T>();
			string[] names = Enum.GetNames<SA1Character>();

			for (int i = 0; i < names.Count(); i++)
			{
				string filename = SA1StageInfo.GetFilename(levelid, actid, names[i], isCamFile);
				string filepath = Path.Combine(directory, filename);
				if (File.Exists(filepath))
					files.Add(names[i], ImportFile<T>(filepath));
			}

			return files;
		}

		/// <summary>
		/// Automatic SA1 SET File Import.
		/// </summary>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		public static Dictionary<string, SETFile> ImportSA1SETFileAuto(string directory, string levelid, string actid)
		{
			return ImportSA1File<SETFile>(directory, levelid, actid, false);
		}

		/// <summary>
		/// Automatic SA1 CAM File Import.
		/// </summary>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		public static Dictionary<string, SA1CAMFile> ImportSA1CAMFileAuto(string directory, string levelid, string actid)
		{
			return ImportSA1File<SA1CAMFile>(directory, levelid, actid, true);
		}

		/// <summary>
		/// Automatic SA2 File Imports using a Directory, Level ID, and Act ID.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		private static List<T> ImportSA2File<T>(string directory, string levelid, string actid, bool isCamFile) where T : IBinaryFile<T>
		{
			List<T> files = new List<T>();

			string filename = SA2StageInfo.GetFilename(levelid, actid, SA2ChaoRaceLevel.None.ToString(), isCamFile);
			string filepath = Path.Combine(directory, filename);
			if (File.Exists(filepath))
				files.Add(T.FromFile(filepath));

			return files;
		}

		/// <summary>
		/// Automatic SA2 SET File Import.
		/// </summary>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		public static Dictionary<string, SETFile> ImportSA2SETFileAuto(string directory, string levelid, string actid)
		{
			Dictionary<string, SETFile> files = new Dictionary<string, SETFile>();

			string filename = SA2StageInfo.GetFilename(levelid, actid, SA2ChaoRaceLevel.None.ToString(), false);

			string filename_s = $"{filename}_s";
			string filepath_s = Path.Combine(directory, filename_s);
			string filename_u = $"{filename}_u";
			string filepath_u = Path.Combine(directory, filename_u);

			if (File.Exists($"{filepath_s}.bin"))
				files.Add(filename_s, SETFile.FromFile($"{filepath_s}.bin"));
			if (File.Exists($"{filepath_u}.bin"))
				files.Add(filename_u, SETFile.FromFile($"{filepath_u}.bin"));

			return files;
		}

		/// <summary>
		/// Automatic SA2 CAM File Import.
		/// </summary>
		/// <param name="directory"></param>
		/// <param name="levelid"></param>
		/// <param name="actid"></param>
		/// <returns></returns>
		public static List<SA2CAMFile> ImportSA2CAMFileAuto(string directory, string levelid, string actid)
		{
			return ImportSA2File<SA2CAMFile>(directory, levelid, actid, true);
		}

		#endregion
	}
}
