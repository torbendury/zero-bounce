CREATE TABLE IF NOT EXISTS categories(
    id SERIAL,
    name VARCHAR(250) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS entries(
    id SERIAL,
    name VARCHAR(250) NOT NULL,
    categoryId INT NOT NULL,
    visibleToPlayer BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fkCategory
        FOREIGN KEY (categoryId)
        REFERENCES categories(id)
)