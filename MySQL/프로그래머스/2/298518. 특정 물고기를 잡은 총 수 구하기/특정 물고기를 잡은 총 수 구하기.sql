SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO fish_info
JOIN FISH_NAME_INFO fish_name
    ON fish_info.FISH_TYPE = fish_name.FISH_TYPE
WHERE fish_name.FISH_NAME = 'BASS' OR fish_name.FISH_NAME = 'SNAPPER';