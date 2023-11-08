1
 create or replace function summa_products()
 returns integer as $$
begin
     return (select sum(price) from supermarket_products);
 end;
 $$ language plpgsql;

 select summa_products()

2
  create or replace function average_products()
   returns integer as $$
  begin
       return (select avg(price) from supermarket_products);
   end;
   $$ language plpgsql;

   select average_products()


--3
-- create or replace function get_min_max_product_price()
-- returns table (min_price numeric, max_price numeric)  language plpgsql as $$

--  begin
--  return query 
--   select
--    max(price),
--    min(price)
--   from
--    supermarket_products;
-- end;$$
-- SELECT * from get_min_max_product_price();

--4
-- create or replace function vychislenya(x numeric, y numeric, z numeric)
-- returns numeric language plpgsql as $$
-- begin
-- return (x* y * z)/5;
-- end;$$ 

-- select round(vychislenya(6, 7, 13.4),2)



--5
-- create or replace function find_category()
-- returns table (product_name text, price integer) as $$
-- begin
--     return query
--     select product_name, price
--     from supermarket_products
--     join categories
-- 	on p.category_id = c.category_id
--     where c.category_name = c.category_name
--     and price > 3;
-- END;
-- $$ LANGUAGE plpgsql;

-- select * from find_category();


--6
-- create or replace function products_1(product_name text, quantity integer)
-- returns table(product_name text, quantity_1 integer) as $$
-- begin 
--     return query
-- 	select p.product_name, p.quantity
-- 	from supermarket_products 
-- 	where p.product_name = product_name and p.quantity < quantity_1;
-- end;
-- $$ language plpgsql;
-- select * from products_1('Milk', 10);

--7
-- create or replace function perimeter_area(diameter numeric)
-- returns table (area numeric, perimeter numeric) as $$
-- begin
-- return query 
-- select (0.25 * 3.14 * diameter * diameter) as area,
-- (3.14 * diameter) as perimeter;
-- end;
-- $$ language plpgsql;
-- select * from perimeter_area(10)


--8
-- create or replace function area_triangle(a integer, c integer)
-- returns numeric as $$
-- begin
-- return 
--     (c^2 * sqrt(4 * a^2 - c^2)) /4 as area;
-- end;
-- $$ language plpgsql;
-- select * from area_triangle(5, 6)
