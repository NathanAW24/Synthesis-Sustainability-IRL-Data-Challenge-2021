/******Keywords
'#sgfood', '#sustainable', '#sgfoodies', 
'#singaporefood', '#goodfoodpeoplesg', '#vegan', 
'#meatless', '#plantbasedfoods', '#eatwideawake', 
'#homecoking', '#cookingmadeeasy', '#plantbaseddiet', 
'#igsgfoodies', '#goodfoodpeople', '#vegetarian', 
'#sustainability', 
'#crustsingapore', '#goodpeople', '#upcycle', '#foodphotography'  ******/


SELECT [post_type],[post_caption],[post_hashtags],[post_comments],[post_likes],[segment_name]
FROM [Sustainability_Challenge_DB].[dbo].[Event_Data_IG]
WHERE [post_hashtags] LIKE '%#sgfood%'
OR [post_hashtags] LIKE '%#sustainable%'
OR [post_hashtags] LIKE '%#sgfoodies%'
OR [post_hashtags] LIKE '%#singaporefood%'
OR [post_hashtags] LIKE '%#goodfoodpeoplesg%'
OR [post_hashtags] LIKE '%#vegan%'
OR [post_hashtags] LIKE '%#meatless%'
OR [post_hashtags] LIKE '%#plantbasedfoods%'
OR [post_hashtags] LIKE '%#eatwideawake%'
OR [post_hashtags] LIKE '%#homecoking%'
OR [post_hashtags] LIKE '%#cookingmadeeasy%'
OR [post_hashtags] LIKE '%#plantbaseddiet%'
OR [post_hashtags] LIKE '%#igsgfoodies%'
OR [post_hashtags] LIKE '%#goodfoodpeople%'
OR [post_hashtags] LIKE '%#vegetarian%'
OR [post_hashtags] LIKE '%#sustainability%'
OR [post_hashtags] LIKE '%#crustsingapore%'
OR [post_hashtags] LIKE '%#goodpeople%'
OR [post_hashtags] LIKE '%#upcycle%'
OR [post_hashtags] LIKE '%#foodphotography%'
ORDER BY [post_likes] DESC
