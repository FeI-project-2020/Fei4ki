CREATE TABLE IF NOT EXISTS discount (
    id SERIAL PRIMARY KEY,
    srv_name VARCHAR(30) NOT NULL,
    discount_percent NUMERIC(4,2) 
);

CREATE TABLE IF NOT EXISTS classroom (
    classroom_number INT NOT NULL,
    addr VARCHAR(50) NOT NULL,
    floor INT NOT NULL,
    map_path TEXT
);

CREATE TABLE IF NOT EXISTS authentificated_user (
    user_id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    pswd VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS comment (
    comment_id BIGSERIAL PRIMARY KEY,
    txt VARCHAR(30) NOT NULL,
    posted_time TIMESTAMP NOT NULL,
    CONSTRAINT fk_comment_id FOREIGN KEY (comment_id) REFERENCES authentificated_user (user_id)
);

CREATE TABLE IF NOT EXISTS teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    rating NUMERIC(15,5) 
);

CREATE TABLE IF NOT EXISTS teacher_comment (
    t_teacher_id BIGINT,  
    teacher_comment_id BIGINT,
    PRIMARY KEY (t_teacher_id),
    CONSTRAINT pk_t_teacher_id FOREIGN KEY (t_teacher_id) REFERENCES teacher (teacher_id),
    CONSTRAINT fk_teacher_comment_id FOREIGN KEY (teacher_comment_id) REFERENCES comment (comment_id)
);

CREATE TABLE IF NOT EXISTS news (
    news_id BIGSERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    author VARCHAR(30) NOT NULL,
    txt VARCHAR(30) NOT NULL,
    posted_time TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS news_comment (
    n_news_id BIGINT,
    news_comment_id BIGINT,
    PRIMARY KEY (n_news_id),
    CONSTRAINT pk_n_news_id FOREIGN KEY (n_news_id) REFERENCES news (news_id),
    CONSTRAINT fk_news_comment_id FOREIGN KEY (news_comment_id) REFERENCES comment (comment_id)
);

CREATE TABLE IF NOT EXISTS student (
    studentskyi_num NUMERIC(8,0) UNIQUE NOT NULL,
    student_id BIGINT,
    PRIMARY KEY (student_id),
    CONSTRAINT pk_studentskyi_num FOREIGN KEY (student_id) REFERENCES authentificated_user (user_id)
);