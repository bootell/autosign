drop table if exists tasks;
create table tasks (
    task_id integer primary key autoincrement,
    task_name varchar not null,
    task_status int not null
);
