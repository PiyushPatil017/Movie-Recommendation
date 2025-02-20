import streamlit as st
import pickle


movie_df = pickle.load(open('Movies Dataset.pkl','rb'))
movie_list = movie_df['title'].tolist()
similarity = pickle.load(open('similarity.pkl','rb'))

movie_title = []
movie_poster = []

def recommend(option):
    movie_index = movie_df[movie_df['title'] == option].index[0]
    recommended_movies_index = sorted(enumerate(similarity[movie_index]),key = lambda x: x[1], reverse = True)[0:21]

    for i in recommended_movies_index:
        movie_title.append(movie_df['title'].iloc[i[0]])
        movie_poster.append(movie_df['image_url'].iloc[i[0]])
    return movie_title, movie_poster
st.title('Movie Recommendation')
option = st.selectbox('Select Your Movie',movie_list)

if st.button('Recommend'):
    movie_tile, movie_poster = recommend(option)

    col1, col2,col3,col4= st.columns(4)
    with col1:
        st.image(movie_poster[1], caption = movie_title[1] )
    with col2:
        st.image(movie_poster[2], caption = movie_title[2] )
    with col3:
        st.image(movie_poster[3], caption = movie_title[3] )
    with col4:
        st.image(movie_poster[4], caption = movie_title[4] )


    col5, col6,col7,col8 = st.columns(4)
    with col5:
        st.image(movie_poster[5],caption = movie_title[5] )
    with col6:
        st.image(movie_poster[6], caption = movie_title[6] )
    with col7:
        st.image(movie_poster[7], caption = movie_title[7] )
    with col8:
        st.image(movie_poster[8], caption = movie_title[8] )


    col9, col10, col11, col12 = st.columns(4)
    with col9:
        st.image(movie_poster[9], caption = movie_title[9] )
    with col10:
        st.image(movie_poster[10], caption = movie_title[10] )
    with col11:
        st.image(movie_poster[11], caption = movie_title[11] )
    with col12:
        st.image(movie_poster[12], caption = movie_title[12] )

    col13, col14, col15, col16 = st.columns(4)
    with col9:
        st.image(movie_poster[13], caption=movie_title[13])
    with col10:
        st.image(movie_poster[14], caption=movie_title[14])
    with col11:
        st.image(movie_poster[15], caption=movie_title[15])
    with col12:
        st.image(movie_poster[16], caption=movie_title[16])

    col17, col18, col19, col20 = st.columns(4)
    with col9:
        st.image(movie_poster[17], caption=movie_title[17])
    with col10:
        st.image(movie_poster[18], caption=movie_title[18])
    with col11:
        st.image(movie_poster[19], caption=movie_title[19])
    with col12:
        st.image(movie_poster[20], caption=movie_title[20])
else:
    st.write('Press Recommend')


