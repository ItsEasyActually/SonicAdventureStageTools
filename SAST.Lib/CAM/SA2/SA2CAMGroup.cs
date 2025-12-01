using SAST.Lib.CAM.SA1;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SAST.Lib.CAM.SA2
{
	public class SA2CAMGroup
	{
		#region Internal
		#region Variables
		#region Cameras Variable
		/// <summary>
		/// List of <see cref="SA2CAMObject"/>.
		/// </summary>
		protected List<SA2CAMObject> Cameras = new List<SA2CAMObject>();

		/// <summary>
		/// Total number of <see cref="SA2CAMObject"/>s in the <see cref="SA2CAMGroup"/>
		/// </summary>
		public int CameraCount { get { return Cameras.Count; } }

		/// <summary>
		/// Adds a <see cref="SA2CAMObject"/> to the <see cref="SA2CAMGroup"/>'s Cameras.
		/// </summary>
		/// <param name="camera"></param>
		public void AddCamera(SA2CAMObject camera) { Cameras.Add(camera); }

		/// <summary>
		/// Removes the supplied <see cref="SA2CAMObject"/> from the <see cref="SA2CAMGroup"/>'s Cameras.
		/// </summary>
		/// <param name="camera"></param>
		public void RemoveCamera(SA2CAMObject camera) { Cameras.Remove(camera); }

		/// <summary>
		/// Removes the <see cref="SA2CAMObject"/> at the supplied index from the <see cref="SA2CAMGroup"/>'s Cameras.
		/// </summary>
		/// <param name="index"></param>
		public void RemoveCamera(int index) { Cameras.RemoveAt(index); }

		/// <summary>
		/// Clears the <see cref="SA2CAMGroup"/>'s Cameras.
		/// </summary>
		public void ClearCameras() { Cameras.Clear(); }

		/// <summary>
		/// Gets the <see cref="SA2CAMGroup"/>'s Cameras.
		/// </summary>
		/// <returns>A copy of the Cameras List.</returns>
		public List<SA2CAMObject> GetCameras() { return Cameras; }

		#endregion

		#region Point Variable
		/// <summary>
		/// List of <see cref="SA2PointObject"/>.
		/// </summary>
		protected List<SA2PointObject> Points = new List<SA2PointObject>();

		/// <summary>
		/// Total number of <see cref="SA2PointObject"/>s in the <see cref="SA2CAMGroup"/>.
		/// </summary>
		public int PointCount { get { return Points.Count; } }

		/// <summary>
		/// Adds a <see cref="SA2PointObject"/> to the <see cref="SA2CAMGroup"/>'s Points.
		/// </summary>
		/// <param name="point"></param>
		public void AddPoint(SA2PointObject point) { Points.Add(point); }

		/// <summary>
		/// Removes the supplied <see cref="SA2PointObject"/> from the <see cref="SA2CAMGroup"/>'s Points.
		/// </summary>
		/// <param name="point"></param>
		public void RemovePoint(SA2PointObject point) { Points.Remove(point); }

		/// <summary>
		/// Removes a <see cref="SA2PointObject"/> at the supplied index from the <see cref="SA2CAMGroup"/>'s Points.
		/// </summary>
		/// <param name="index"></param>
		public void RemovePoint(int index) { Points.RemoveAt(index); }

		/// <summary>
		/// Clears the <see cref="SA2CAMGroup"/>'s Points. 
		/// </summary>
		public void ClearPoints() { Points.Clear(); }

		/// <summary>
		/// Gets the <see cref="SA2CAMGroup"/>'s Points.
		/// </summary>
		/// <returns>A copy of the Points List.</returns>
		public List<SA2PointObject> GetPoints() { return Points; }

		#endregion

		#endregion

		#region Constructors
		/// <summary>
		/// Default Constructor.
		/// </summary>
		public SA2CAMGroup() { }

		#endregion

		#region Functions
		/// <summary>
		/// Clears the <see cref="Cameras"/> and <see cref="Points"/> Lists.
		/// </summary>
		public void Clear()
		{
			ClearCameras();
			ClearPoints();
		}

		#endregion
		#endregion
	}
}
