using System.Diagnostics.CodeAnalysis;

namespace SAST.Lib.DataTypes
{
	public abstract class Vector<T>
	{
		[AllowNull]
		public T X;

		[AllowNull]
		public T Y;

		[AllowNull]
		public T Z;

		public override string ToString()
		{
			if (X != null && Y != null && Z != null)
				return $"{X}, {Y}, {Z}";
			else
				return "Vector has null variables!";
		}
	}
}
