namespace SAST.Lib.IO
{
	/// <summary>
	/// Interface implementing Stream and File reading/writing functions.
	/// </summary>
	public interface IBinaryFile<T>
	{
		/// <summary>
		/// Method for writing to a <see cref="MemoryStream"/>.
		/// </summary>
		/// <param name="stream">Stream to be written to.</param>
		/// <param name="isBigEndian">Sets if the file should be written as Big Endian.</param>
		public void ToStream(MemoryStream stream, bool isBigEndian = false);

		/// <summary>
		/// Method for writing to a file.
		/// </summary>
		/// <param name="path">Path to the file to be saved.</param>
		/// <param name="isBigEndian">Sets if the file should be written as Big Endian.</param>
		public void ToFile(string path, bool isBigEndian = false);

		/// <summary>
		/// Static method for reading from a <see cref="MemoryStream"/>.
		/// </summary>
		/// <typeparam name="T"><see cref="T"/></typeparam>
		/// <param name="stream">Stream to be read from.</param>
		/// <returns>A new object of <see cref="T"/>.</returns>
		public static abstract T FromStream(MemoryStream stream);

		/// <summary>
		/// Static method for reading from a file.
		/// </summary>
		/// <typeparam name="T"><see cref="T"/></typeparam>
		/// <param name="path">Path to the file to read.</param>
		/// <returns>A new object of <see cref="T"/>.</returns>
		public static abstract T FromFile(string path);
	}
}
