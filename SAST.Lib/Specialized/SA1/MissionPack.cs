using SAST.Lib.CAM.SA1;
using SAST.Lib.SET;
using System;
using System.Collections.Generic;
using System.Text;

namespace SAST.Lib.Specialized.SA1
{
	public class MissionPack
	{
		#region Variables
		public SETFile SetFile { get; set; } = new SETFile();

		public MissionParameterFile PRMFile { get; set; } = new MissionParameterFile();

		public SA1CAMFile CamFile { get; set; } = new SA1CAMFile();

		#endregion

		#region Constructors
		public MissionPack() { }

		public MissionPack(string folderpath, string filename)
		{
			string fullpath = Path.GetFullPath(folderpath);
			if (Path.Exists(fullpath))
			{
				string setFile = Path.Combine(fullpath, $"SET{filename}");
				string prmFile = Path.Combine(fullpath, $"PRM{filename}");
				string camFile = Path.Combine(fullpath, $"CAM{filename}");

				SetFile = SETFile.FromFile(setFile);
				PRMFile = MissionParameterFile.FromFile(prmFile);
				CamFile = SA1CAMFile.FromFile(camFile);
			}
		}

		#endregion

		#region Functions
		/// <summary>
		/// Writes the mission related SET, PRM, and CAM files to the supplied folder using the suffix to the filename provided.
		/// </summary>
		/// <param name="folderpath"></param>
		/// <param name="filename"></param>
		public void WriteFiles(string folderpath, string filename)
		{
			string fullpath = Path.GetFullPath( folderpath);
			if (Path.Exists(fullpath))
			{
				if (SetFile.ObjectCount == PRMFile.Count)
				{
					string setFile = Path.Combine(fullpath, $"SET{filename}");
					string prmFile = Path.Combine(fullpath, $"PRM{filename}");
					string camFile = Path.Combine(fullpath, $"CAM{filename}");

					SetFile.ToFile(setFile);
					PRMFile.ToFile(prmFile);
					CamFile.ToFile(camFile);
				}
				else
					Console.WriteLine($"Mission files [{filename}] do not have a matching count of Object and Parameter objects. Aborting writing files.");
			}
			else
				Console.WriteLine($"{fullpath} does not exist. Aborting writing files.");
		}

		#endregion
	}
}
