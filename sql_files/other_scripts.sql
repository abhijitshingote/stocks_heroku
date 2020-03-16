

/*
CLEANUP STOCK PRICE HISTORY
*/
drop table if exists public.price_history;
create table public.price_history
(
symbol varchar(10),
date_traded date,
open_price float,
high_price float,
low_price float,
close_price float,
volume bigint
);
insert into public.price_history (symbol, date_traded, open_price, high_price, low_price, close_price, volume)
select sph.symbol,sph."Date",trunc(sph."Open"::numeric,2),trunc(sph."High"::numeric,2),trunc(sph."Low"::numeric,2),trunc(sph."Close"::numeric,2),sph."Volume"
from public.stock_price_history sph ;



drop function if exists public.get_return() ;
CREATE FUNCTION get_return() RETURNS void AS $$
    #variable_conflict use_variable
    DECLARE
        curtime timestamp := now();
    BEGIN
   
drop table if exists public.return_1_day;
create table return_1_day
as 
select today.symbol,s.sector,s.industry,s.marketcap,s.symbolname,today.date_traded,today.close_price as latest_close,prior.close_price as prior_close,
round(((100*(today.close_price - prior.close_price)/prior.close_price)::numeric),2) as return_percentage, now() as timestamp_updated
from (
select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded) from public.price_history)) as today

inner join (select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded)-1 from public.price_history) ) as prior
on today.symbol=prior.symbol
inner join  public.stockinfo s on (today.symbol=s.symbol);	    



drop table if exists public.return_7_day;
create table return_7_day
as 
select today.symbol,s.sector,s.industry,s.marketcap,s.symbolname,today.date_traded,today.close_price as latest_close,prior.close_price as prior_close,
round(((100*(today.close_price - prior.close_price)/prior.close_price)::numeric),2) as return_percentage, now() as timestamp_updated
from (
select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded) from public.price_history)) as today

inner join (select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded)-7 from public.price_history) ) as prior
on today.symbol=prior.symbol
inner join  public.stockinfo s on (today.symbol=s.symbol);	

drop table if exists public.return_14_day;
create table return_14_day
as 
select today.symbol,s.sector,s.industry,s.marketcap,s.symbolname,today.date_traded,today.close_price as latest_close,prior.close_price as prior_close,
round(((100*(today.close_price - prior.close_price)/prior.close_price)::numeric),2) as return_percentage, now() as timestamp_updated
from (
select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded) from public.price_history)) as today

inner join (select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded)-14 from public.price_history) ) as prior
on today.symbol=prior.symbol
inner join  public.stockinfo s on (today.symbol=s.symbol);	

drop table if exists public.return_30_day;
create table return_30_day
as 
select today.symbol,s.sector,s.industry,s.marketcap,s.symbolname,today.date_traded,today.close_price as latest_close,prior.close_price as prior_close,
round(((100*(today.close_price - prior.close_price)/prior.close_price)::numeric),2) as return_percentage, now() as timestamp_updated
from (
select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded) from public.price_history)) as today

inner join (select  ph.date_traded,ph.symbol,ph.close_price
from public.price_history ph
where ph.date_traded=(select max(date_traded)-30 from public.price_history) ) as prior
on today.symbol=prior.symbol
inner join  public.stockinfo s on (today.symbol=s.symbol);	

drop table if exists public.total_return;
create table total_return
as 
select d1.symbol,d1.sector,d1.industry,d1.marketcap,d1.symbolname,d1.date_traded,d1.latest_close,
d1.prior_close,d1.return_percentage as return_1_day,d7.return_percentage as return_7_day,d14.return_percentage as return_14_day,
d30.return_percentage as return_30_day,now() as timestamp_updated
from public.return_1_day d1
left join public.return_7_day d7 on (d1.symbol=d7.symbol)
left join public.return_14_day d14 on (d1.symbol=d14.symbol)
left join public.return_30_day d30 on (d1.symbol=d30.symbol);

    END
$$ 	LANGUAGE plpgsql;

SELECT public.get_return();



