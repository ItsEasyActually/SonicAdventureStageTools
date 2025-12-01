using Kermalis.EndianBinaryIO;
using SAST.Lib.Extensions;
using SAST.Lib.IO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SAST.Lib.CAM.SA2
{
	public class SA2CAMFile : IBinarySerializable, IBinaryFile<SA2CAMFile>
	{
		#region Internal
		#region Enums
		public enum ContentFlags : int
		{
			HasNoContent = 0,
			HasCameras = 2,
			HasPoints = 3,
			HasDemoCameras = 4,
			HasDemoPoints = 5,
			HasMultiplayerCameras = 6,
			HasMultiplayerPoints = 7,
		}

		#endregion

		#region Variables
		/// <summary>
		/// Content found within the file. 
		/// </summary>
		public ContentFlags Content;

		public SA2CAMGroup SinglePlayerCameraGroup { get; set; } = new SA2CAMGroup();

		public SA2CAMGroup DemoCameraGroup { get; set; } = new SA2CAMGroup();

		public SA2CAMGroup MultiplayerCameraGroup { get; set; } = new SA2CAMGroup();

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SA2CAMFile"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			endianBinaryReader.CheckEndianByUInt32();
			Content = endianBinaryReader.ReadEnum<ContentFlags>();

			// Opted to just check all of the data in the event a camera file's content flag doesn't match the actual contents.
			// Anyone loading data can perform a check against the Content flag and what data is populated if they want to verify the contents.
			int sizeSPCameras = endianBinaryReader.ReadInt32();
			int sizeSPPoints = endianBinaryReader.ReadInt32();
			int sizeDCameras = endianBinaryReader.ReadInt32();
			int sizeDPoints = endianBinaryReader.ReadInt32();
			int sizeMPCameras = endianBinaryReader.ReadInt32();
			int sizeMPPoints = endianBinaryReader.ReadInt32();

			int curAddr = 0x20;

			if (sizeSPCameras > 0)
			{
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);
				endianBinaryReader.CheckEndianByUInt32();   // This check has to be run due to the port sometimes having left over Little Endian data.

				for (int i = 0; i < (sizeSPCameras / SA2CAMObject.Size); i++)
				{
					SA2CAMObject cam = endianBinaryReader.ReadObject<SA2CAMObject>();
					if (!cam.IsEmpty())
						SinglePlayerCameraGroup.AddCamera(cam);
					else
						break;
				}
			}

			if (sizeSPPoints > 0)
			{
				curAddr += sizeSPCameras;
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);

				for (int i = 0; i < (sizeSPPoints / SA2PointObject.Size); i++)
				{
					SA2PointObject point = endianBinaryReader.ReadObject<SA2PointObject>();
					if (!point.IsEmpty())
						SinglePlayerCameraGroup.AddPoint(point);
					else
						break;
				}
			}

			if (sizeDCameras > 0)
			{
				curAddr += sizeSPPoints;
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);
				endianBinaryReader.CheckEndianByUInt32();   // This check has to be run due to the port sometimes having left over Little Endian data.

				for (int i = 0; i < (sizeDCameras / SA2CAMObject.Size); i++)
				{
					SA2CAMObject cam = endianBinaryReader.ReadObject<SA2CAMObject>();
					if (!cam.IsEmpty())
						DemoCameraGroup.AddCamera(cam);
					else
						break;
				}
			}

			if (sizeDPoints > 0)
			{
				curAddr += sizeDCameras;
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);

				for (int i = 0; i < (sizeDPoints / SA2PointObject.Size); i++)
				{
					SA2PointObject point = endianBinaryReader.ReadObject<SA2PointObject>();
					if (!point.IsEmpty())
						DemoCameraGroup.AddPoint(point);
					else
						break;
				}
			}

			if (sizeMPCameras > 0)
			{
				curAddr += sizeDPoints;
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);
				endianBinaryReader.CheckEndianByUInt32();   // This check has to be run due to the port sometimes having left over Little Endian data.

				for (int i = 0; i < (sizeMPCameras / SA2CAMObject.Size); i++)
				{
					SA2CAMObject cam = endianBinaryReader.ReadObject<SA2CAMObject>();
					if (!cam.IsEmpty())
						MultiplayerCameraGroup.AddCamera(cam);
					else
						break;
				}
			}

			if (sizeMPPoints > 0)
			{
				curAddr += sizeMPCameras;
				endianBinaryReader.Stream.Seek(curAddr, SeekOrigin.Begin);

				for (int i = 0; i < (sizeMPPoints / SA2PointObject.Size); i++)
				{
					SA2PointObject point = endianBinaryReader.ReadObject<SA2PointObject>();
					if (!point.IsEmpty())
						MultiplayerCameraGroup.AddPoint(point);
					else
						break;
				}
			}
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SA2CAMFile"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			if (MultiplayerCameraGroup.PointCount > 0)
				Content = ContentFlags.HasMultiplayerPoints;
			else if (MultiplayerCameraGroup.CameraCount > 0)
				Content = ContentFlags.HasMultiplayerCameras;
			else if (DemoCameraGroup.PointCount > 0)
				Content = ContentFlags.HasDemoPoints;
			else if (DemoCameraGroup.CameraCount > 0)
				Content = ContentFlags.HasDemoCameras;
			else if (SinglePlayerCameraGroup.PointCount > 0)
				Content = ContentFlags.HasPoints;
			else if (SinglePlayerCameraGroup.CameraCount > 0)
				Content = ContentFlags.HasCameras;
			else
				Content = ContentFlags.HasNoContent;

			endianBinaryWriter.WriteEnum(Content);
			endianBinaryWriter.WriteInt32(SinglePlayerCameraGroup.CameraCount * SA2CAMObject.Size);
			endianBinaryWriter.WriteInt32(SinglePlayerCameraGroup.PointCount * SA2PointObject.Size);
			endianBinaryWriter.WriteInt32(DemoCameraGroup.CameraCount * SA2CAMObject.Size);
			endianBinaryWriter.WriteInt32(DemoCameraGroup.PointCount * SA2PointObject.Size);
			endianBinaryWriter.WriteInt32(MultiplayerCameraGroup.CameraCount * SA2CAMObject.Size);
			endianBinaryWriter.WriteInt32(MultiplayerCameraGroup.PointCount * SA2PointObject.Size);
			endianBinaryWriter.WriteZeroes(4);

			foreach (SA2CAMObject cam in SinglePlayerCameraGroup.GetCameras())
				endianBinaryWriter.WriteObject(cam);

			foreach (SA2PointObject point in SinglePlayerCameraGroup.GetPoints())
				endianBinaryWriter.WriteObject(point);

			foreach (SA2CAMObject cam in DemoCameraGroup.GetCameras())
				endianBinaryWriter.WriteObject(cam);

			foreach (SA2PointObject point in DemoCameraGroup.GetPoints())
				endianBinaryWriter.WriteObject(point);

			foreach (SA2CAMObject cam in MultiplayerCameraGroup.GetCameras())
				endianBinaryWriter.WriteObject(cam);

			foreach (SA2PointObject point in MultiplayerCameraGroup.GetPoints())
				endianBinaryWriter.WriteObject(point);
		}

		public void SwapRotations()
		{
			if (SinglePlayerCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in SinglePlayerCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
				}
			}

			if (DemoCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in DemoCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
				}
			}
			
			if (MultiplayerCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in MultiplayerCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.ZXY, DataTypes.RotationVector.AxisOrder.XYZ);
				}
			}
		}

		public void SwapRotationsBack()
		{
			if (SinglePlayerCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in SinglePlayerCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
				}
			}

			if (DemoCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in DemoCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
				}
			}

			if (MultiplayerCameraGroup.CameraCount > 0)
			{
				foreach (SA2CAMObject cam in MultiplayerCameraGroup.GetCameras())
				{
					cam.Collision.Rotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
					cam.CameraRotation.SwapAxisOrder(DataTypes.RotationVector.AxisOrder.XYZ, DataTypes.RotationVector.AxisOrder.ZXY);
				}
			}
		}

		public void ToStream(MemoryStream stream, bool isBigEndian = false) { FileWriter.WriteStream(stream, this, isBigEndian); }

		public void ToFile(string path, bool isBigEndian = false)
		{
			if (SinglePlayerCameraGroup.CameraCount > 0 || MultiplayerCameraGroup.CameraCount > 0)
				FileWriter.WriteCompressedFile(path, this, isBigEndian);
			else
				Console.WriteLine("SA2CAMFile has no Single Player or Multiplayer Cameras. Nothing to save!");
		}

		#endregion
		#endregion

		#region Static
		#region Functions
		public static SA2CAMFile FromStream(MemoryStream stream) { return FileReader.ReadStream<SA2CAMFile>(stream); }

		public static SA2CAMFile FromFile(string path) { return FileReader.ReadCompressedFile<SA2CAMFile>(path); }

		#endregion

		#endregion
	}
}
