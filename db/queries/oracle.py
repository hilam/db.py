queries = {
    "column": {
        "head": "select {column} from {table} limit {n};",
        "all": "select {column} from {table};",
        "unique": "select distinct {column} from {table};",
        "sample": "select {column} from {table} order by dbms_random.value limit {n};"
    },
    "table": {
        "select": "select {columns} from {table};",
        "head": "select * from {table} limit {n};",
        "all": "select * from {table};",
        "unique": "select distinct {columns} from {table};",
        "sample": "select * from {table} order by dbms_random.value limit {n};"
    },
    "system": {
        "schema_no_system": """
                select
                    table_name
                    , column_name
                    , data_type
                from
                    all_tab_columns
                where
                    owner not in ('SYS', 'SYSTEM')
                """,
        "schema_with_system": """
                select
                    table_name
                    , column_name
                    , data_type
                from
                    all_tab_columns;
                """,
        "schema_specified": """
                select
                    table_name
                    , column_name
                    , data_type
                from
                    all_tab_columns
                where owner in (%s);
                """,
        "foreign_keys_for_table": """
                select 
                    b.column_name
                    , c.table_name
                    , c.column_name
                from all_cons_columns b,
                     all_cons_columns c,
                     all_constraints a
                where b.constraint_name = a.constraint_name
                 and a.owner           = b.owner
                 and b.position        = c.position
                 and c.constraint_name = a.r_constraint_name
                 and c.owner           = a.r_owner
                 and a.constraint_type = 'R'
                 and b.table_name ='%s';
        """,
        "foreign_keys_for_column": """
                select 
                    b.column_name
                    , c.table_name
                    , c.column_name
                from all_cons_columns b,
                     all_cons_columns c,
                     all_constraints a
                where b.constraint_name = a.constraint_name
                 and a.owner           = b.owner
                 and b.position        = c.position
                 and c.constraint_name = a.r_constraint_name
                 and c.owner           = a.r_owner
                 and a.constraint_type = 'R'
                 and b.column_name = '%s';
        """,
        "ref_keys_for_table": """
                select 
                    b.column_name
                    , c.table_name
                    , c.column_name
                from all_cons_columns b,
                     all_cons_columns c,
                     all_constraints a
                where b.constraint_name = a.constraint_name
                 and a.owner           = b.owner
                 and b.position        = c.position
                 and c.constraint_name = a.r_constraint_name
                 and c.owner           = a.r_owner
                 and a.constraint_type = 'R'
                 and c.table_name ='%s';
        """
    }
}
