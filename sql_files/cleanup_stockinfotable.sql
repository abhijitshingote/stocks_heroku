/*
CLEANUP STOCK INFO
*/
SELECT pg_catalog.set_config('search_path', 'public', false);
drop table if exists public.stockinfo_new;
create table public.stockinfo_new 
(
stockinfo_id serial primary key,
symbol varchar(10),
marketcap float,
symbolname varchar(200),
sector varchar(200),
industry varchar(200)
) ;
insert into public.stockinfo_new (symbol, marketcap, symbolname, sector, industry)
select s.symbol,TRUNC(s."marketCap"::numeric/1000000000,2),s."shortName" ,s.sector ,s.industry
from public.stockinfo s  ;

update public.stockinfo_new si 
set sector=(select replace(si2.sector,' ','_') 
from public.stockinfo_new si2 where si2.stockinfo_id=si.stockinfo_id);
update public.stockinfo_new si 
set sector='Unknown' where trim(sector)='' or sector is NULL;

drop table if exists public.stockinfo;
ALTER TABLE public.stockinfo_new   RENAME TO stockinfo;

