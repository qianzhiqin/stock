create table stock
(
  id         INTEGER not null
    constraint table_name_pk
      primary key autoincrement,
  stock      VARCHAR,
  type       VARCHAR,
  price      REAL,
  source     VARCHAR,
  userid     VARCHAR,
  user       VARCHAR,
  date       VARCHAR,
  proportion VARCHAR,
  createTime VARCHAR
);


create table user
(
  id         INTEGER not null
    constraint table_name_pk
      primary key autoincrement,
  userId     VARCHAR,
  user       VARCHAR,
  source     VARCHAR,
  proportion VARCHAR,
  createTime VARCHAR,
  updateTime VARCHAR
);


