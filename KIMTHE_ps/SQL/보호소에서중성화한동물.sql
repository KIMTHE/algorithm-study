SELECT ins.animal_id, ins.animal_type, ins.name
from animal_ins ins
inner join animal_outs outs
on ins.animal_id = outs.animal_id
where sex_upon_intake like '%Intact%' and sex_upon_outcome not like '%Intact%'
