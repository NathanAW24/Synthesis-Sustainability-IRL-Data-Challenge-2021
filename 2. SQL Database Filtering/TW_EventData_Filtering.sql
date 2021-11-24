/****** KEYWORDS
['surplusfood', 'Courtauld2025', 'makegoodhappen', 'christmasleftovers', 'plantbased']

******/

SELECT [post_content],[post_is_retweet],[post_is_truncated],[post_like_count],
[post_retweet_count],[post_media],[post_hashtags],[post_reply_to_post_id],[segment_name]
FROM [Sustainability_Challenge_DB].[dbo].[Event_Data_TW]
WHERE [post_hashtags] LIKE '%surplusfood%'
OR [post_hashtags] LIKE '%Courtauld2025%'
OR [post_hashtags] LIKE '%christmasleftovers%'
OR [post_hashtags] LIKE '%plantbased%'
ORDER BY cast([post_retweet_count] as int) DESC
