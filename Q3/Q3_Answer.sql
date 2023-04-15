SELECT 
    o.owner_id,
    o.owner_name,
    COUNT(DISTINCT c.category_id) AS different_category_count
FROM 
    owner o
    JOIN article a ON o.owner_id = a.owner_id
    JOIN category_article_mapping cam ON a.article_id = cam.article_id
    JOIN category c ON cam.category_id = c.category_id
GROUP BY 
    o.owner_id,
    o.owner_name
ORDER BY 
    different_category_count DESC;
