import streamlit as st

import os

import asyncio

async def Home():
    st.title('Welcome to Discovrio Final Project APP')
    st.write('Check This Out: [Github Repository](https://github.com/Radityofajar/Final-Project-DS40)')

    st.header("Meet Our Team!")

    team_members = {
        "[Radityo Fajar](https://www.linkedin.com/in/radityo-fajar-pamungkas/)": "Teams/radityo.jpg",
        "Nugroho Wahyu Saputre": "Teams/dummy.jpg",
        "Puteri Sakinah Mantikasari A.G": "Teams/dummy.jpg",
        "Scudetto Ciano Syam": "Teams/dummy.jpg",
        "Rima Fitrianti Azahra": "Teams/dummy.jpg",
        "[Farhad Salim Sungkar](https://www.linkedin.com/in/farhad-salim-sungkar-834126292/)": "Teams/farhad.jpg",
        "Yayes Kasnanda Bintang": "Teams/dummy.jpg",
    }

    # Create a grid for team members
    num_members = len(team_members)
    cols = 4  # Number of columns
    rows = 2  # number of rows needed

    for i in range(rows):
        cols_list = st.columns(cols)  # Create columns for this row
        for j in range(cols):
            index = i * cols + j  # Calculate index for team member
            if index < num_members:  # Check if the index is valid
                name = list(team_members.keys())[index]
                image_path = team_members[name]
                with cols_list[j]:
                    st.image(image_path, use_column_width=True)
                    st.write(name)
  
    st.header('Song Popularity Dataset: Attributes')
    st.write("Check the dataset here: [dataset link](https://www.kaggle.com/datasets/yasserh/song-popularity-dataset)")
    attributes = {
        "acousticness": (
            "A confidence measure from 0.0 to 1.0 of whether the track is acoustic. "
            "1.0 represents high confidence the track is acoustic."
        ),
        "danceability": (
            "Danceability describes how suitable a track is for dancing based on a combination of "
            "musical elements including tempo, rhythm stability, beat strength, and overall regularity. "
            "A value of 0.0 is least danceable and 1.0 is most danceable."
        ),
        "duration_ms": (
            "The duration of the track in milliseconds."
        ),
        "energy": (
            "Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. "
            "Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, "
            "while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute "
            "include dynamic range, perceived loudness, timbre, onset rate, and general entropy."
        ),
        "instrumentalness": (
            "Predicts whether a track contains no vocals. 'Ooh' and 'aah' sounds are treated as instrumental in this context. "
            "Rap or spoken word tracks are clearly 'vocal'. The closer the instrumentalness value is to 1.0, the "
            "greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent "
            "instrumental tracks, but confidence is higher as the value approaches 1.0."
        ),
        "key": (
            "The key the track is in. Integers map to pitches using standard [Pitch Class](https://en.wikipedia.org/wiki/Pitch_class) notation. "
            "E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. "
        ),
        "liveness": (
            "Detects the presence of an audience in the recording. Higher liveness values represent an "
            "increased probability that the track was performed live. A value above 0.8 provides strong likelihood "
            "that the track is live."
        ),
        "loudness": (
            "The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire "
            "track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound "
            "that is the primary psychological correlate of physical strength (amplitude). Values typically range "
            "between -60 and 0 dB."
        ),
        "mode": (
            "Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content "
            "is derived. Major is represented by 1 and minor is 0."
        ),
        "speechiness": (
            "Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the "
            "recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 "
            "describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe "
            "tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. "
            "Values below 0.33 most likely represent music and other non-speech-like tracks."
        ),
        "tempo": (
            "The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is "
            "the speed or pace of a given piece and derives directly from the average beat duration."
        ),
        "time_signature": (
            "An estimated time signature. The time signature (meter) is a notational convention to specify how many beats "
            "are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of '3/4', to '7/4'."
        ),
    }

    # Display the attribute descriptions
    for attr, description in attributes.items():
        st.subheader(attr)
        st.write(description)
