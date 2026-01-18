USE [login_system]
GO

/****** Object:  Table [dbo].[students]    Script Date: 13-01-2026 23:00:52 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[students](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[StudentID] [int] NULL,
	[name] [varchar](100) NULL,
	[age] [int] NULL,
	[email] [varchar](100) NULL,
	[Department] [varchar](100) NULL,
	[GPA] [decimal](3, 2) NULL,
	[GraduationYear] [int] NULL,
	[password] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_students_email] UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[teachers]    Script Date: 13-01-2026 23:04:18 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[teachers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](100) NULL,
	[Education] [varchar](100) NULL,
	[JoiningYear] [int] NULL,
	[ExperienceInCurrentDomain] [int] NULL,
	[LeaveOrNot] [bit] NULL,
	[email] [varchar](100) NULL,
	[password] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[videos]    Script Date: 19-01-2026 02:56:28 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[videos](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[title] [varchar](255) NULL,
	[description] [varchar](max) NULL,
	[subject] [varchar](100) NULL,
	[video_url] [varchar](max) NULL,
	[duration] [int] NULL,
	[status] [varchar](20) NULL,
	[teacher_id] [int] NULL,
	[created_at] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[videos] ADD  DEFAULT (getdate()) FOR [created_at]
GO

ALTER TABLE [dbo].[videos]  WITH CHECK ADD  CONSTRAINT [FK_videos_teachers] FOREIGN KEY([teacher_id])
REFERENCES [dbo].[teachers] ([id])
GO

ALTER TABLE [dbo].[videos] CHECK CONSTRAINT [FK_videos_teachers]
GO

/****** Object:  Table [dbo].[video_views]    Script Date: 19-01-2026 02:59:16 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[video_views](
	[video_id] [int] NOT NULL,
	[student_id] [int] NOT NULL,
	[watch_time] [int] NULL,
	[id] [int] IDENTITY(1,1) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_video_student] UNIQUE NONCLUSTERED 
(
	[video_id] ASC,
	[student_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[video_views]  WITH CHECK ADD  CONSTRAINT [FK_video_views_students] FOREIGN KEY([student_id])
REFERENCES [dbo].[students] ([id])
GO

ALTER TABLE [dbo].[video_views] CHECK CONSTRAINT [FK_video_views_students]
GO

ALTER TABLE [dbo].[video_views]  WITH CHECK ADD  CONSTRAINT [FK_video_views_videos] FOREIGN KEY([video_id])
REFERENCES [dbo].[videos] ([id])
GO

ALTER TABLE [dbo].[video_views] CHECK CONSTRAINT [FK_video_views_videos]
GO

/****** Object:  Table [dbo].[video_notes]    Script Date: 19-01-2026 02:59:58 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[video_notes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[video_id] [int] NULL,
	[language] [varchar](10) NULL,
	[content] [varchar](max) NULL,
	[created_at] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_video_language] UNIQUE NONCLUSTERED 
(
	[video_id] ASC,
	[language] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[video_notes] ADD  DEFAULT (getdate()) FOR [created_at]
GO

ALTER TABLE [dbo].[video_notes]  WITH CHECK ADD  CONSTRAINT [FK_video_notes_videos] FOREIGN KEY([video_id])
REFERENCES [dbo].[videos] ([id])
GO

ALTER TABLE [dbo].[video_notes] CHECK CONSTRAINT [FK_video_notes_videos]
GO


