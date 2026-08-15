using SAST.Lib.CAM.SA1;
using SAST.Lib.CAM.SA2;
using SAST.Lib.GameInfo;
using SAST.Lib.IO;
using SAST.Lib.SET;

namespace SAST.Lib.Blender
{
	public static class ExportManager
	{
		/// <summary>
		/// Exports a file if <typeparamref name="T"/> is a valid <see cref="IBinaryFile{T}"/>
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="item"></param>
		/// <param name="path"></param>
		/// <param name="bigEndian"></param>
		private static void ExportFile<T>(T item, string path, bool bigEndian) where T : IBinaryFile<T>
		{
			item.ToFile(path, bigEndian);
		}

		#region Manual Export
		/// <summary>
		/// Exports a <see cref="SETFile"/>.
		/// </summary>
		/// <param name="file"></param>
		/// <param name="path"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSETFile(SETFile file, string path, bool bigEndian) { ExportFile<SETFile>(file, path, bigEndian); }

		/// <summary>
		/// Exports two <see cref="SETFile"/>s from a single supplied SET file.
		/// </summary>
		/// <param name="file"></param>
		/// <param name="path"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA2SETFile(SETFile file, string path, bool bigEndian)
		{
			string extension = Path.GetExtension(path);
			string filename = Path.GetFileNameWithoutExtension(path);
			string directory = Path.GetFullPath(Path.GetDirectoryName(path));

			SETFile sfile = new SETFile();
			SETFile ufile = new SETFile();

			foreach (var item in file.GetObjects())
			{
				if (item.Flags.HasFlag(SETObject.SetFlags.Flag4))
					ufile.AddObject(item);
				else
					sfile.AddObject(item);
			}

			string sfilepath = Path.Combine(directory, $"{filename}_s{extension}");
			string ufilepath = Path.Combine(directory, $"{filename}_u{extension}");

			ExportFile<SETFile>(sfile, sfilepath, bigEndian);
			ExportFile<SETFile>(ufile, ufilepath, bigEndian);
		}

		/// <summary>
		/// Exports a <see cref="SA1CAMFile"/>.
		/// </summary>
		/// <param name="file"></param>
		/// <param name="path"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA1CamFile(SA1CAMFile file, string path, bool bigEndian) { ExportFile<SA1CAMFile>(file, path, bigEndian); }

		/// <summary>
		/// Exports a <see cref="SA2CAMFile"/>.
		/// </summary>
		/// <param name="file"></param>
		/// <param name="path"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA2CamFile(SA2CAMFile file, string path, bool bigEndian)
		{
			file.SwapRotationsBack();
			ExportFile<SA2CAMFile>(file, path, bigEndian);
		}

		#endregion

		#region Automatic Export
		/// <summary>
		/// Exports a file for Sonic Adventure 1/DX.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		private static void ExportSA1FileAuto<T>(Dictionary<string, T> files, string directory, string stageID, string actID, bool bigEndian, bool isCameraFile) where T : IBinaryFile<T>
		{
			if (Directory.Exists(directory))
			{
				foreach (var file in files)
				{
					string filename = SA1StageInfo.GetFilename(stageID, actID, file.Key, isCameraFile);

					string filepath = Path.Combine(directory, filename);

					ExportFile<T>(file.Value, filepath, bigEndian);
				}
			}
		}

		/// <summary>
		/// Exports a <see cref="SETFile"/> for Sonic Adventure 1/DX.
		/// </summary>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA1SETFileAuto(Dictionary<string, SETFile> files, string directory, string stageID, string actID, bool bigEndian)
		{
			ExportSA1FileAuto<SETFile>(files, directory, stageID, actID, bigEndian, false);
		}

		/// <summary>
		/// Exports a <see cref="SA1CAMFile"/> for Sonic Adventure 1/DX.
		/// </summary>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA1CamFileAuto(Dictionary<string, SA1CAMFile> files, string directory, string stageID, string actID, bool bigEndian)
		{
			ExportSA1FileAuto<SA1CAMFile>(files, directory, stageID, actID, bigEndian, true);
		}

		/// <summary>
		/// Exports a file for Sonic Adventure 2/Battle.
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		private static void ExportSA2FileAuto<T>(List<T> files, string directory, string stageID, string actID, bool bigEndian) where T: IBinaryFile<T>
		{
			if (Directory.Exists(directory))
			{
				foreach (var file in files)
				{
					string filename = SA2StageInfo.GetFilename(stageID, actID, "None", true);

					string filepath = Path.Combine(directory, filename);

					ExportFile<T>(file, filepath, bigEndian);
				}
			}
		}

		/// <summary>
		/// Exports a <see cref="SETFile"/> for Sonic Adventure 2/Battle.
		/// </summary>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA2SETFileAuto(List<SETFile> files, string directory, string stageID, string actID, int mode, bool bigEndian)
		{
			ExportSA2FileAuto<SETFile>(files, directory, stageID, actID, bigEndian);

			if (Directory.Exists(directory))
			{
				foreach (var file in files)
				{
					string filename = SA2StageInfo.GetFilename(stageID, actID, "None", true);

					switch (mode)
					{
						case 1:
							filename = $"{filename}_2p.bin";
							break;
						case 2:
							filename = $"{filename}_hd.bin";
							break;
					}

					string filepath = Path.Combine(directory, filename);

					ExportSA2SETFile(file, filepath, bigEndian);
				}
			}
		}

		/// <summary>
		/// Exports a <see cref="SA2CAMFile"/> for Sonic Adventure 2/Battle.
		/// </summary>
		/// <param name="files"></param>
		/// <param name="directory"></param>
		/// <param name="stageID"></param>
		/// <param name="actID"></param>
		/// <param name="bigEndian"></param>
		public static void ExportSA2CamFileAuto(List<SA2CAMFile> files, string directory, string stageID, string actID, bool bigEndian)
		{
			ExportSA2FileAuto<SA2CAMFile>(files, directory, stageID, actID, bigEndian);
		}

		#endregion
	}
}
