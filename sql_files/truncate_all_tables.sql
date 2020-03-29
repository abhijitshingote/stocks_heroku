SELECT pg_catalog.set_config('search_path', 'public', false);
truncate table public.stockinfo, public.stock_price_history,
public.price_history, public.return_1_day, public.return_7_day,
public.return_14_day, public.return_30_day, public.total_return ;