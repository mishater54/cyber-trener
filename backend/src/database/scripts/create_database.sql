use master
go

if db_id('cyber_trainer') is null
begin
	create database cyber_trainer
end
go