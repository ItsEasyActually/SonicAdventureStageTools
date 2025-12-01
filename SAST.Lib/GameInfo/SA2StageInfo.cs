using System.Text;

namespace SAST.Lib.GameInfo
{
	public enum SA2Stage
	{
		TestStage		= 0,
		SonicTest		= 1,
		KnucklesTest	= 2,
		GreenForest		= 3,
		WhiteJungle		= 4,
		PumpkinHill		= 5,
		SkyRail			= 6,
		AquaticMine		= 7,
		SecurityHall	= 8,
		PrisonLane		= 9,
		MetalHarbor		= 10,
		IronGate		= 11,
		WeaponsBed		= 12,
		CityEscape		= 13,
		RadicalHighway	= 14,
		WeaponsBed2P	= 15,
		WildCanyon		= 16,
		MissionStreet	= 17,
		DryLagoon		= 18,
		SonicShadow1	= 19,
		TailsEggman1	= 20,
		SandOcean		= 21,
		CrazyGadget		= 22,
		HiddenBase		= 23,
		EternalEngine	= 24,
		DeathChamber	= 25,
		EggQuarters		= 26,
		LostColony		= 27,
		PyramidCave		= 28,
		TailsEggman2	= 29,
		FinalRush		= 30,
		GreenHill		= 31,
		MeteorHerd		= 32,
		KnucklesRouge	= 33,
		CannonsCoreS	= 34,
		CannonsCoreE	= 35,
		CannonsCoreT	= 36,
		CannonsCoreR	= 37,
		CannonsCoreK	= 38,
		MissionStreet2P	= 39,
		FinalChase		= 40,
		WildCanyon2P	= 41,
		SonicShadow2	= 42,
		CosmicWall		= 43,
		MadSpace		= 44,
		SandOcean2P		= 45,
		DryLagoon2P		= 46,
		PyramidRace		= 47,
		HiddenBase2P	= 48,
		PoolQuest		= 49,
		PlanetQuest		= 50,
		DeckRace		= 51,
		DowntownRace	= 52,
		CosmicWall2P	= 53,
		GrindRace		= 54,
		LostColony2P	= 55,
		EternalEngine2P	= 56,
		MetalHarbor2P	= 57,
		IronGate2P		= 58,
		DeathChamber2P	= 59,
		BossBigFoot		= 60,
		BossHotshot		= 61,
		BossFlyingDog	= 62,
		BossKingBoomBoo	= 63,
		BossEggGolemS	= 64,
		BossBiolizard	= 65,
		BossFinalHazard	= 66,
		BossEggGolemE	= 67,
		// 68
		// 69
		StoryKart		= 70,
		KartRace		= 71,
		// 72-89
		ChaoWorld		= 90
	}

	public enum SA2Act
	{
		None,
		Tails,
		Rouge,
		Easy,
		Intermediate,
		Hard,
		ChaoRaceNeutral,
		ChaoRaceHero,
		ChaoRaceDark
	}

	public enum SA2ChaoRaceLevel
	{
		None,
		BeginnerFly,
		BeginnerPower,
		BeginnerRun,
		BeginnerSwim,
		JewelFly,
		JewelPower,
		JewelRun,
		JewelSwim,
		JewelL,
		JewelLong
	}

	public static class SA2StageInfo
	{
		private class Filenames
		{
			public string SetName = string.Empty;
			public string CamName = string.Empty;

			public Filenames(string set, string cam)
			{
				SetName = set;
				CamName = cam;
			}
		}

		private static Dictionary<SA2Stage, Filenames> stageIDs = new Dictionary<SA2Stage, Filenames>()
		{
			{ SA2Stage.TestStage,		new Filenames(((int)SA2Stage.TestStage).ToString("D4"),			((int)SA2Stage.TestStage).ToString("D2"))		},
			{ SA2Stage.SonicTest,       new Filenames(((int)SA2Stage.SonicTest).ToString("D4"),			((int)SA2Stage.SonicTest).ToString("D2"))		},
			{ SA2Stage.KnucklesTest,    new Filenames(((int)SA2Stage.KnucklesTest).ToString("D4"),		((int)SA2Stage.KnucklesTest).ToString("D2"))	},
			{ SA2Stage.GreenForest,     new Filenames(((int)SA2Stage.GreenForest).ToString("D4"),		((int)SA2Stage.GreenForest).ToString("D2"))		},
			{ SA2Stage.WhiteJungle,     new Filenames(((int)SA2Stage.WhiteJungle).ToString("D4"),		((int)SA2Stage.WhiteJungle).ToString("D2"))		},
			{ SA2Stage.PumpkinHill,     new Filenames(((int)SA2Stage.PumpkinHill).ToString("D4"),		((int)SA2Stage.PumpkinHill).ToString("D2"))		},
			{ SA2Stage.SkyRail,         new Filenames(((int)SA2Stage.SkyRail).ToString("D4"),			((int)SA2Stage.SkyRail).ToString("D2"))			},
			{ SA2Stage.AquaticMine,     new Filenames(((int)SA2Stage.AquaticMine).ToString("D4"),		((int)SA2Stage.AquaticMine).ToString("D2"))		},
			{ SA2Stage.SecurityHall,    new Filenames(((int)SA2Stage.SecurityHall).ToString("D4"),		((int)SA2Stage.SecurityHall).ToString("D2"))	},
			{ SA2Stage.PrisonLane,      new Filenames(((int)SA2Stage.PrisonLane).ToString("D4"),		((int)SA2Stage.PrisonLane).ToString("D2"))		},
			{ SA2Stage.MetalHarbor,     new Filenames(((int)SA2Stage.MetalHarbor).ToString("D4"),		((int)SA2Stage.MetalHarbor).ToString("D2"))		},
			{ SA2Stage.IronGate,        new Filenames(((int)SA2Stage.IronGate).ToString("D4"),			((int)SA2Stage.IronGate).ToString("D2"))		},
			{ SA2Stage.WeaponsBed,      new Filenames(((int)SA2Stage.WeaponsBed).ToString("D4"),		((int)SA2Stage.WeaponsBed).ToString("D2"))		},
			{ SA2Stage.CityEscape,      new Filenames(((int)SA2Stage.CityEscape).ToString("D4"),		((int)SA2Stage.CityEscape).ToString("D2"))		},
			{ SA2Stage.RadicalHighway,  new Filenames(((int)SA2Stage.RadicalHighway).ToString("D4"),	((int)SA2Stage.RadicalHighway).ToString("D2"))	},
			{ SA2Stage.WeaponsBed2P,    new Filenames(((int)SA2Stage.WeaponsBed2P).ToString("D4"),		((int)SA2Stage.WeaponsBed2P).ToString("D2"))	},
			{ SA2Stage.WildCanyon,      new Filenames(((int)SA2Stage.WildCanyon).ToString("D4"),		((int)SA2Stage.WildCanyon).ToString("D2"))		},
			{ SA2Stage.MissionStreet,   new Filenames(((int)SA2Stage.MissionStreet).ToString("D4"),		((int)SA2Stage.MissionStreet).ToString("D2"))	},
			{ SA2Stage.DryLagoon,       new Filenames(((int)SA2Stage.DryLagoon).ToString("D4"),			((int)SA2Stage.DryLagoon).ToString("D2"))		},
			{ SA2Stage.SonicShadow1,    new Filenames(((int)SA2Stage.SonicShadow1).ToString("D4"),		((int)SA2Stage.SonicShadow1).ToString("D2"))	},
			{ SA2Stage.TailsEggman1,    new Filenames(((int)SA2Stage.TailsEggman1).ToString("D4"),		((int)SA2Stage.TailsEggman1).ToString("D2"))	},
			{ SA2Stage.SandOcean,       new Filenames(((int)SA2Stage.SandOcean).ToString("D4"),			((int)SA2Stage.SandOcean).ToString("D2"))		},
			{ SA2Stage.CrazyGadget,     new Filenames(((int)SA2Stage.CrazyGadget).ToString("D4"),		((int)SA2Stage.CrazyGadget).ToString("D2"))		},
			{ SA2Stage.HiddenBase,      new Filenames(((int)SA2Stage.HiddenBase).ToString("D4"),		((int)SA2Stage.HiddenBase).ToString("D2"))		},
			{ SA2Stage.EternalEngine,   new Filenames(((int)SA2Stage.EternalEngine).ToString("D4"),		((int)SA2Stage.EternalEngine).ToString("D2"))	},
			{ SA2Stage.DeathChamber,    new Filenames(((int)SA2Stage.DeathChamber).ToString("D4"),		((int)SA2Stage.DeathChamber).ToString("D2"))	},
			{ SA2Stage.EggQuarters,     new Filenames(((int)SA2Stage.EggQuarters).ToString("D4"),		((int)SA2Stage.EggQuarters).ToString("D2"))		},
			{ SA2Stage.LostColony,      new Filenames(((int)SA2Stage.LostColony).ToString("D4"),		((int)SA2Stage.LostColony).ToString("D2"))		},
			{ SA2Stage.PyramidCave,     new Filenames(((int)SA2Stage.PyramidCave).ToString("D4"),		((int)SA2Stage.PyramidCave).ToString("D2"))		},
			{ SA2Stage.TailsEggman2,    new Filenames(((int)SA2Stage.TailsEggman2).ToString("D4"),		((int)SA2Stage.TailsEggman2).ToString("D2"))	},
			{ SA2Stage.FinalRush,       new Filenames(((int)SA2Stage.FinalRush).ToString("D4"),			((int)SA2Stage.FinalRush).ToString("D2"))		},
			{ SA2Stage.GreenHill,       new Filenames(((int)SA2Stage.GreenHill).ToString("D4"),			((int)SA2Stage.GreenHill).ToString("D2"))		},
			{ SA2Stage.MeteorHerd,      new Filenames(((int)SA2Stage.MeteorHerd).ToString("D4"),		((int)SA2Stage.MeteorHerd).ToString("D2"))		},
			{ SA2Stage.KnucklesRouge,   new Filenames(((int)SA2Stage.KnucklesRouge).ToString("D4"),		((int)SA2Stage.KnucklesRouge).ToString("D2"))	},
			{ SA2Stage.CannonsCoreS,    new Filenames(((int)SA2Stage.CannonsCoreS).ToString("D4"),		((int)SA2Stage.CannonsCoreS).ToString("D2"))	},
			{ SA2Stage.CannonsCoreE,    new Filenames(((int)SA2Stage.CannonsCoreE).ToString("D4"),		((int)SA2Stage.CannonsCoreE).ToString("D2"))	},
			{ SA2Stage.CannonsCoreT,    new Filenames(((int)SA2Stage.CannonsCoreT).ToString("D4"),		((int)SA2Stage.CannonsCoreT).ToString("D2"))	},
			{ SA2Stage.CannonsCoreR,    new Filenames(((int)SA2Stage.CannonsCoreR).ToString("D4"),		((int)SA2Stage.CannonsCoreR).ToString("D2"))	},
			{ SA2Stage.CannonsCoreK,    new Filenames(((int)SA2Stage.CannonsCoreK).ToString("D4"),		((int)SA2Stage.CannonsCoreK).ToString("D2"))	},
			{ SA2Stage.MissionStreet2P, new Filenames(((int)SA2Stage.MissionStreet2P).ToString("D4"),	((int)SA2Stage.MissionStreet2P).ToString("D2")) },
			{ SA2Stage.FinalChase,      new Filenames(((int)SA2Stage.FinalChase).ToString("D4"),		((int)SA2Stage.FinalChase).ToString("D2"))		},
			{ SA2Stage.WildCanyon2P,    new Filenames(((int)SA2Stage.WildCanyon2P).ToString("D4"),		((int)SA2Stage.WildCanyon2P).ToString("D2"))	},
			{ SA2Stage.SonicShadow2,    new Filenames(((int)SA2Stage.SonicShadow2).ToString("D4"),		((int)SA2Stage.SonicShadow2).ToString("D2"))	},
			{ SA2Stage.CosmicWall,      new Filenames(((int)SA2Stage.CosmicWall).ToString("D4"),		((int)SA2Stage.CosmicWall).ToString("D2"))		},
			{ SA2Stage.MadSpace,        new Filenames(((int)SA2Stage.MadSpace).ToString("D4"),			((int)SA2Stage.MadSpace).ToString("D2"))		},
			{ SA2Stage.SandOcean2P,     new Filenames(((int)SA2Stage.SandOcean2P).ToString("D4"),		((int)SA2Stage.SandOcean2P).ToString("D2"))		},
			{ SA2Stage.DryLagoon2P,     new Filenames(((int)SA2Stage.DryLagoon2P).ToString("D4"),		((int)SA2Stage.DryLagoon2P).ToString("D2"))		},
			{ SA2Stage.PyramidRace,     new Filenames(((int)SA2Stage.PyramidRace).ToString("D4"),		((int)SA2Stage.PyramidRace).ToString("D2"))		},
			{ SA2Stage.HiddenBase2P,    new Filenames(((int)SA2Stage.HiddenBase2P).ToString("D4"),		((int)SA2Stage.HiddenBase2P).ToString("D2"))	},
			{ SA2Stage.PoolQuest,       new Filenames(((int)SA2Stage.PoolQuest).ToString("D4"),			((int)SA2Stage.PoolQuest).ToString("D2"))		},
			{ SA2Stage.PlanetQuest,     new Filenames(((int)SA2Stage.PlanetQuest).ToString("D4"),		((int)SA2Stage.PlanetQuest).ToString("D2"))		},
			{ SA2Stage.DeckRace,        new Filenames(((int)SA2Stage.DeckRace).ToString("D4"),			((int)SA2Stage.DeckRace).ToString("D2"))		},
			{ SA2Stage.DowntownRace,    new Filenames(((int)SA2Stage.DowntownRace).ToString("D4"),		((int)SA2Stage.DowntownRace).ToString("D2"))	},
			{ SA2Stage.CosmicWall2P,    new Filenames(((int)SA2Stage.CosmicWall2P).ToString("D4"),		((int)SA2Stage.CosmicWall2P).ToString("D2"))	},
			{ SA2Stage.GrindRace,       new Filenames(((int)SA2Stage.GrindRace).ToString("D4"),			((int)SA2Stage.GrindRace).ToString("D2"))		},
			{ SA2Stage.LostColony2P,    new Filenames(((int)SA2Stage.LostColony2P).ToString("D4"),		((int)SA2Stage.LostColony2P).ToString("D2"))	},
			{ SA2Stage.EternalEngine2P, new Filenames(((int)SA2Stage.EternalEngine2P).ToString("D4"),	((int)SA2Stage.EternalEngine2P).ToString("D2")) },
			{ SA2Stage.MetalHarbor2P,   new Filenames(((int)SA2Stage.MetalHarbor2P).ToString("D4"),		((int)SA2Stage.MetalHarbor2P).ToString("D2"))	},
			{ SA2Stage.IronGate2P,      new Filenames(((int)SA2Stage.IronGate2P).ToString("D4"),		((int)SA2Stage.IronGate2P).ToString("D2"))		},
			{ SA2Stage.DeathChamber2P,  new Filenames(((int)SA2Stage.DeathChamber2P).ToString("D4"),	((int)SA2Stage.DeathChamber2P).ToString("D2"))	},
			{ SA2Stage.BossBigFoot,     new Filenames("_b_bigfoot",										((int)SA2Stage.BossBigFoot).ToString("D2"))		},
			{ SA2Stage.BossHotshot,     new Filenames("_b_hotshot",										((int)SA2Stage.BossHotshot).ToString("D2"))		},
			{ SA2Stage.BossFlyingDog,   new Filenames("_b_fdog",										((int)SA2Stage.BossFlyingDog).ToString("D2"))	},
			{ SA2Stage.BossKingBoomBoo, new Filenames("_b_bigbogy",										((int)SA2Stage.BossKingBoomBoo).ToString("D2")) },
			{ SA2Stage.BossEggGolemS,   new Filenames("_b_golem",										((int)SA2Stage.BossEggGolemS).ToString("D2"))	},
			{ SA2Stage.BossBiolizard,   new Filenames("_b_last1",										((int)SA2Stage.BossBiolizard).ToString("D2"))	},
			{ SA2Stage.BossFinalHazard, new Filenames("_b_last2",										((int)SA2Stage.BossFinalHazard).ToString("D2")) },
			{ SA2Stage.BossEggGolemE,   new Filenames("_b_golem_e",										((int)SA2Stage.BossEggGolemE).ToString("D2"))	},
			{ SA2Stage.StoryKart,       new Filenames("cart",											((int)SA2Stage.StoryKart).ToString("D2"))		},
			{ SA2Stage.KartRace,        new Filenames("cart",											((int)SA2Stage.KartRace).ToString("D2"))		},
			{ SA2Stage.ChaoWorld,       new Filenames("chao",											((int)SA2Stage.ChaoWorld).ToString("D2"))		},
		};

		private static Dictionary<SA2Act, string> actIDs = new Dictionary<SA2Act, string>()
		{
			{ SA2Act.Tails,				"tails" },
			{ SA2Act.Rouge,				"rouge" },
			{ SA2Act.Easy,				"mini1" },
			{ SA2Act.Intermediate,		"mini2" },
			{ SA2Act.Hard,				"mini3" },
			{ SA2Act.ChaoRaceNeutral,	"landneut" },
			{ SA2Act.ChaoRaceHero,		"landhero" },
			{ SA2Act.ChaoRaceDark,		"landdark" },
		};

		private static Dictionary<SA2ChaoRaceLevel, string> chaoRaceIDs = new Dictionary<SA2ChaoRaceLevel, string>()
		{
			{ SA2ChaoRaceLevel.BeginnerFly,		"BegFly" },
			{ SA2ChaoRaceLevel.BeginnerPower,	"BegPow" },
			{ SA2ChaoRaceLevel.BeginnerRun,		"BegRun" },
			{ SA2ChaoRaceLevel.BeginnerSwim,	"BegSwm" },
			{ SA2ChaoRaceLevel.JewelFly,		"JwlFly" },
			{ SA2ChaoRaceLevel.JewelPower,      "JwlPow" },
			{ SA2ChaoRaceLevel.JewelRun,        "JwlRun" },
			{ SA2ChaoRaceLevel.JewelSwim,       "JwlSwm" },
			{ SA2ChaoRaceLevel.JewelL,          "JwlL" },
			{ SA2ChaoRaceLevel.JewelLong,       "JwlLng" },
		};

		private static string GetSetID(SA2Stage stageID, SA2Act actID, SA2ChaoRaceLevel chaoID)
		{
			StringBuilder sb = new StringBuilder();

			switch (stageID)
			{
				default:
					sb.Append("set");
					sb.Append(stageIDs[stageID].SetName);
					break;
				case SA2Stage.StoryKart:
				case SA2Stage.KartRace:
					sb.Append("setcart");
					sb.Append(actIDs[actID]);
					break;
				case SA2Stage.ChaoWorld:
					sb.Append("chaosetrace");
					if (actID == SA2Act.None)
						sb.Append(chaoRaceIDs[chaoID]);
					else
						sb.Append(actIDs[actID]);
					break;
			}

			return sb.ToString();
		}

		private static string GetCamID(SA2Stage stageID, SA2Act actID, SA2ChaoRaceLevel chaoID)
		{
			StringBuilder sb = new StringBuilder();

			switch (stageID)
			{
				default:
					sb.Append("stg");
					sb.Append(stageIDs[stageID].CamName);
					sb.Append("cam.prs");
					break;
				case SA2Stage.ChaoWorld:
					if (actID == SA2Act.None)
					{
						sb.Append("stg");
						sb.Append(stageIDs[stageID].CamName);
						sb.Append("cam.prs");
					}
					else
					{
						sb.Append("chaoracecam");
						sb.Append(chaoRaceIDs[chaoID]);
					}
					break;
			}

			return sb.ToString();
		}

		public static string GetFilename(string stageID, string actID, string chaoID, bool isCamFile)
		{
			StringBuilder sb = new StringBuilder();
			SA2Stage sID = Enum.Parse<SA2Stage>(stageID);
			if (actID == "")
				actID = "None";
			SA2Act aID = Enum.Parse<SA2Act>(actID);
			if (chaoID == "")
				chaoID = "None";
			SA2ChaoRaceLevel cID = Enum.Parse<SA2ChaoRaceLevel>(chaoID);

			if (isCamFile)
				sb.Append(GetCamID(sID, aID, cID));
			else
				sb.Append(GetSetID(sID, aID, cID));

			return sb.ToString();
		}
	}
}
