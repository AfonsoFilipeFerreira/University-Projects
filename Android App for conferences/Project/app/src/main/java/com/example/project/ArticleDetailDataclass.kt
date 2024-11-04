package com.example.project

data class ArticleDetail(
    val id: Int,
    val title: String,
    val authors: String,
    val abstract: String?,
    val pdfLink: String?
)