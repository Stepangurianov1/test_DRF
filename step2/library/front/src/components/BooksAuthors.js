import React from 'react'
import { useParams } from 'react-router-dom'
const BookItem = ({book}) => {
return (
<tr>
<td>
    {book.name}
</td>
<td>
    {book.authors}
</td>
<td>
    {book.id}
</td>
</tr>
)
}

const BookAuthors = ({books}) => {
    let {authorId} = useParams()
    console.log(authorId)
    let filter_books = books.filter((book)=>book.authors.includes(parseInt(authorId)))
    return (
    <table>
    <th>
        Name
    </th>
    <th>
        Authors
    </th>
    <th>
        ID
    </th>
    {filter_books.map((book_) => <BookItem book={book_} />)}
    </table>
    )
}
    export default BookAuthors
    