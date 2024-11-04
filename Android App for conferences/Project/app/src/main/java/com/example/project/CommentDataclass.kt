package com.example.project

data class Comment(
    val id: Int,
    val username: String,
    val articleId: Int,
    val message: String,
    val approved: Int,
    val createdAt: String, // Assuming createdAt is a timestamp
)