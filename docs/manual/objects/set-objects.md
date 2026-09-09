# SET Objects

# Technical Info

## Filename Conventions
In SA1 and SA2, the SET file naming conventions differ due to the lack of different characters per level and SA2 not having any acts. Below is how the names are structured.

=== "SA1"
    ```
    SET[SS][AA][C].bin
    ```
    ??? note "Info"
        SS is the Stage ID, AA is the Act ID, and C is the Character ID.

        Most stages use a 2 digit identifier for the Stage ID and the Act ID. Minigames, some bosses, and Adventure Fields do not.

        For further information, you can check out info on the filenames [here](https://sadocs.unreliable.network/wiki/Sonic_Adventure/CAM_%26_SET_Files)

=== "SA2" 
    ```
    SET[SSSS][_M]_[G].bin
    ```
    ??? note "Info"
        SSSS is the Stage ID, _M is the Mode ID, and G is the Group ID.

        Stage IDs are typically a 4 digit identifier for the stage. Bosses and the Kart stages use unique markers. 

        The Mode ID will either not exist or be for Hard Mode or 2P. Bosses do not use these and only the Story Cart levels use Hard Mode.
        
        * None (e.g. SET0013_S.bin)
        * _HD (e.g. SET0013_HD_S.bin)
        * _2P (e.g. SET0013_2P_S.bin)

        Group ID denotes which grouping of objects the file is for. S for Substansive and U for Unsubstansive. These only differ in their general contents but are all treated exactly the same in-game.

        For further information, you can check out the list [here](https://sadocs.unreliable.network/wiki/Sonic_Adventure_2/Levels)