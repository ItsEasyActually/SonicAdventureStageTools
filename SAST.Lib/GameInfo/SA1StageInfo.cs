using System.Text;

namespace SAST.Lib.GameInfo
{
	public enum SA1Stage
	{
		Practice			= 0,
		EmeraldCoast		= 1,
		WindyValley			= 2,
		TwinklePark			= 3,
		SpeedHighway		= 4,
		RedMountain			= 5,
		SkyDeck				= 6,
		LostWorld			= 7,
		Icecap				= 8,
		Casinopolis			= 9,
		FinalEgg			= 10,
		Mushroom			= 11,
		HotShelter			= 12,
		Jungle				= 13,
		Desert				= 14,
		Chaos0				= 15,
		Chaos2				= 16,
		Chaos4				= 17,
		Chaos6				= 18,
		Chaos7				= 19,
		EggHornet			= 20,
		EggWalker			= 21,
		EggViper			= 22,
		ZERO				= 23,
		E101				= 24,
		E101r				= 25,
		StationSquare		= 26,
		AdvFieldUnused1		= 27,
		AdvFieldUnused2		= 28,
		EggCarrierExterior	= 29,
		AdvFiledUnused3		= 30,
		AdvFieldUnused4		= 31,
		EggCarrierInterior	= 32,
		MysticRuins			= 33,
		ThePast				= 34,
		TwinkleCircuit		= 35,
		SkyChase1			= 36,
		SkyChase2			= 37,
		SandHill			= 38,
		ChaoGardenSS		= 39,
		ChaoGardenMR		= 40,
		ChaoGardenEC		= 41,
		ChaoRace			= 42,
	}

	public enum SA1Act
	{
		Act1 = 0,
		Act2 = 1,
		Act3 = 2,
		Act4 = 3,
		Act5 = 4,
		Act6 = 5,
	}

	public enum SA1Character
	{
		Sonic		= 0,
		Eggman		= 1,
		Tails		= 2,
		Knuckles	= 3,
		Tikal		= 4,
		Amy			= 5,
		Gamma		= 6,
		Big			= 7,
		Last		= 8
	}

	public static class SA1StageInfo
	{
		private static Dictionary<SA1Stage, string> stageIDs = new Dictionary<SA1Stage, string>()
		{
			{ SA1Stage.Practice,			"00"		},
			{ SA1Stage.EmeraldCoast,		"01"		},
			{ SA1Stage.WindyValley,			"02"		},
			{ SA1Stage.TwinklePark,			"03"		},
			{ SA1Stage.SpeedHighway,		"04"		},
			{ SA1Stage.RedMountain,			"05"		},
			{ SA1Stage.SkyDeck,				"06"		},
			{ SA1Stage.LostWorld,			"07"		},
			{ SA1Stage.Icecap,				"08"		},
			{ SA1Stage.Casinopolis,			"09"		},
			{ SA1Stage.FinalEgg,			"10"		},
			{ SA1Stage.HotShelter,			"12"		},
			{ SA1Stage.Chaos0,				"15"		},
			{ SA1Stage.Chaos2,				"16"		},
			{ SA1Stage.Chaos4,				"17"		},
			{ SA1Stage.Chaos6,				"18"		},
			{ SA1Stage.Chaos7,				"19"		},
			{ SA1Stage.EggHornet,			"EGM1"		},
			{ SA1Stage.EggWalker,			"EGM2"		},
			{ SA1Stage.EggViper,			"EGM3"		},
			{ SA1Stage.ZERO,				"ZERO"		},
			{ SA1Stage.E101,				"E101"		},
			{ SA1Stage.E101r,				"E101R"		},
			{ SA1Stage.StationSquare,		"SS"		},
			{ SA1Stage.EggCarrierExterior,	"EC0"		},
			{ SA1Stage.EggCarrierInterior,	"EC3"		},
			{ SA1Stage.MysticRuins,			"MR"		},
			{ SA1Stage.ThePast,				"PAST"		},
			{ SA1Stage.TwinkleCircuit,		"MCART"		},
			{ SA1Stage.SkyChase1,			"SHT1"		},
			{ SA1Stage.SkyChase2,			"SHT2"		},
			{ SA1Stage.SandHill,			"SBOARD"	},
			{ SA1Stage.ChaoGardenSS,		"GARDEN00"	},
			{ SA1Stage.ChaoGardenMR,		"GARDEN01"	},
			{ SA1Stage.ChaoGardenEC,		"GARDEN02"	},
			{ SA1Stage.ChaoRace,			"AL_RACE"	},
		};

		private static Dictionary<SA1Character, string> characterIDs = new Dictionary<SA1Character, string>()
		{
			{ SA1Character.Sonic,		"S"		},
			{ SA1Character.Eggman,		"EG"	},
			{ SA1Character.Tails,		"M"		},
			{ SA1Character.Knuckles,	"K"		},
			{ SA1Character.Tikal,		"TI"	},
			{ SA1Character.Amy,			"A"		},
			{ SA1Character.Gamma,		"E"		},
			{ SA1Character.Big,			"B"		},
			{ SA1Character.Last,		"L"		}
		};

		private static string GetActID(SA1Stage stageID, SA1Act actID)
		{
			switch (stageID)
			{
				default:
					return ((int)actID).ToString("D2");
				case SA1Stage.EggCarrierExterior:
				case SA1Stage.EggCarrierInterior:
					return ((int)actID).ToString("D1");
				case SA1Stage.SkyChase1:
				case SA1Stage.SkyChase2:
				case SA1Stage.ChaoGardenSS:
				case SA1Stage.ChaoGardenMR:
				case SA1Stage.ChaoGardenEC:
				case SA1Stage.EggHornet:
				case SA1Stage.EggWalker:
				case SA1Stage.EggViper:
				case SA1Stage.ZERO:
				case SA1Stage.E101:
				case SA1Stage.E101r:
					return "";
			}
		}

		private static string GetFileID(string stageID, string actID, string characterID)
		{
			StringBuilder sb = new StringBuilder();

			bool isValidStage = Enum.TryParse<SA1Stage>(stageID, true, out var sID);
			bool isValidAct = Enum.TryParse<SA1Act>(actID, true, out var aID);
			bool isValidCharacter = Enum.TryParse<SA1Character>(characterID, true, out var cID);

			if (isValidStage && isValidAct && isValidCharacter)
			{
				sb.Append(stageIDs[sID]);
				sb.Append(GetActID(sID, aID));
				sb.Append(characterIDs[cID]);
			}
			else
			{
				if (!isValidStage)
					Console.WriteLine($"{stageID} is not a valid Stage ID.");
				else if (!isValidAct)
					Console.WriteLine($"{actID} is not a valid Act ID.");
				else if (!isValidCharacter)
					Console.WriteLine($"{characterID} is not a valid Character ID");
				else
					Console.WriteLine("How did you even trigger this?");
			}

				return sb.ToString();
		}

		public static string GetFilename(string stageId, string actID, string characterID, bool isCamFile)
		{
			StringBuilder sb = new StringBuilder();

			if (isCamFile)
				sb.Append("CAM");
			else
				sb.Append("SET");

			sb.Append(GetFileID(stageId, actID, characterID));
			sb.Append(".bin");

			return sb.ToString();
		}
	}
}
