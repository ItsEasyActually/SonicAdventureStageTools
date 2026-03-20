using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Threading.Tasks;

namespace SAST.Lib.SET
{
	public class SETItem
	{
		#region Enumeration
		/// <summary>
		/// Attribute flags for when the object is being loaded.
		/// </summary>
		[Flags]
		public enum LoadAttributeFlags : short
		{
			/// <summary>
			/// Loads the object using the LoadRange variable as a distance to player.
			/// </summary>
			LoadByDistance = 0x1,

			/// <summary>
			/// Loads the object instantly upon level load regardless of player distance to the object.
			/// </summary>
			LoadInstant = 0x2,

			/// <summary>
			/// Loads the object instantly upon level load regardless of player distance, but it only loads it once.
			/// </summary>
			LoadOnce = 0x4,
		}

		/// <summary>
		/// Level the task is set in within the game.
		/// </summary>
		public enum TaskLevels : byte
		{
			/// <summary>
			/// Top level task, used by cntroller type items (Levels, etc).
			/// </summary>
			Level0 = 0,

			/// <summary>
			/// Secondary top level task, usually used things run by the top level task (Skyboxes, bosses, some non-set level objects).
			/// </summary>
			Level1 = 1,

			/// <summary>
			/// Primarily used for Set Objects
			/// </summary>
			Level2 = 2,

			/// <summary>
			/// Sound Effects and Player Actions, also used for some Set Objects.
			/// </summary>
			Level3 = 3,

			/// <summary>
			/// Effects like explosions and lens flares.
			/// </summary>
			Level4 = 4,

			/// <summary>
			/// Cutscenes and Level Results, sections where players have control disabled mostly.
			/// </summary>
			Level5 = 5,

			/// <summary>
			/// Effects tied to the player and other scene entities.
			/// </summary>
			Level6 = 6,

			/// <summary>
			/// Child tasks
			/// </summary>
			Level7 = 7
		}

		/// <summary>
		/// Flags that control the creation of the task. When set, the corresponding types will also be created with the task.
		/// </summary>
		[Flags]
		public enum TaskCreationFlags : byte
		{
			/// <summary>
			/// Creates a Motion Worker (motionwk) for the task.
			/// </summary>
			MotionWork = 1,

			/// <summary>
			/// Creates a Task Worker (taskwk) for the task.
			/// </summary>
			TaskWork = 2,

			/// <summary>
			/// Creates a Force Worker (forcewk) for the task.
			/// </summary>
			ForceWork = 4,

			/// <summary>
			/// Creates an Any Worker (anywk) for the task.
			/// </summary>
			AnyWork = 8,
		}

		#endregion

		#region Variables
		/// <summary>
		/// Task Creation type for the Object Entry.
		/// </summary>
		public TaskCreationFlags InitializeMode { get; set; } = 0;

		/// <summary>
		/// The level the Object's Task will be setup as.
		/// </summary>
		public TaskLevels TaskLevel { get; set; } = TaskLevels.Level2;

		/// <summary>
		/// Attributes for how an Object is loaded 
		/// </summary>
		public LoadAttributeFlags LoadAttributes { get; set; } = LoadAttributeFlags.LoadByDistance;

		/// <summary>
		/// Distance range used in loading an Object when the <see cref="LoadAttributes"/> is set to <see cref="LoadAttributeFlags.LoadByDistance"/>.
		/// </summary>
		public float LoadRange { get; set; } = 160000.0f;

		/// <summary>
		/// Pointer to the initialization code for the Object.
		/// </summary>
		public string FunctionAddress { get; set; } = "0";

		/// <summary>
		/// ASCII Name of the Object in the Object List.
		/// </summary>
		public string Name { get; set; } = string.Empty;

		#endregion

		#region Constructors
		public SETItem() { }

		#endregion

		public static SETItem Deserialize(string path)
		{
			if (File.Exists(path))
			{
				SETItem item = JsonSerializer.Deserialize<SETItem>(path);
				if (item != null)
					return item;
			}

			return new SETItem();
		}
	}
}
