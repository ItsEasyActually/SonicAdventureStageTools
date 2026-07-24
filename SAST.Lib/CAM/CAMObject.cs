using SAST.Lib.DataTypes;

namespace SAST.Lib.CAM
{
	public abstract class CAMObject
	{
		#region Internal
		#region Variables
		/// <summary>
		/// Priority of the camera in the scene. Higher values take priority.
		/// </summary>
		public int Priority { get; set; } = 0;

		/// <summary>
		/// Position, Rotation, and Scale of the Collision volume.
		/// </summary>
		public Node Collision { get; set; } = new Node();

		/// <summary>
		/// Position of the Camera.
		/// 
		/// Usage may vary per camera type.
		/// </summary>
		public FloatVector CameraPosition { get; set; } = new FloatVector();

		/// <summary>
		/// Rotation of the Camera.
		/// 
		/// Usage may vary per camera type.
		/// </summary>
		public RotationVector CameraRotation { get; set; } = new RotationVector();

		/// <summary>
		/// Position of the Camera's Target
		/// 
		/// Usage may vary per the camera type.
		/// </summary>
		public FloatVector CameraTarget { get; set; } = new FloatVector();

		#endregion

		#region Constructors
		public CAMObject() { }

		#endregion
		#endregion
	}
}
