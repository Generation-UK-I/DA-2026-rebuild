SELECT Gender, SUM(Likes) AS Total_Likes
FROM user_data
GROUP BY Gender;
