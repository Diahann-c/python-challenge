{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f99dd002",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependancies\n",
    "import os\n",
    "import csv\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d3ccad9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#INSTRUCTIONS\n",
    "#The total number of votes cast\n",
    "#A complete list of candidates who received votes\n",
    "#The percentage of votes each candidate won\n",
    "#The total number of votes each candidate won\n",
    "#The winner of the election based on popular vote"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b5dd5395",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ballot ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1323913</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1005842</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1880345</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1600337</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1835994</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ballot ID     County                Candidate\n",
       "0    1323913  Jefferson  Charles Casper Stockham\n",
       "1    1005842  Jefferson  Charles Casper Stockham\n",
       "2    1880345  Jefferson  Charles Casper Stockham\n",
       "3    1600337  Jefferson  Charles Casper Stockham\n",
       "4    1835994  Jefferson  Charles Casper Stockham"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#READ CSV FILE\n",
    "election_data = \"Resources/election_data.csv\"\n",
    "election_df = pd.read_csv(election_data)\n",
    "election_df.head() #testing to ensure that it's reading the csv file "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f6c9971e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#DECLARE VARIABLES \n",
    "total_votes_cast = 0 #will use to store the total votes cast\n",
    "candidates = [] #using a list to store all of the eligible candidates\n",
    "votes = [] \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "cc0bc7e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Charles Casper Stockham' 'Diana DeGette' 'Raymon Anthony Doane']\n"
     ]
    }
   ],
   "source": [
    "#CODE\n",
    "#The total number of votes cast\n",
    "total_votes_cast = len(election_df.index)\n",
    "#otal_votes_cast = election_df.count()\n",
    "total_votes_cast #want to check that the number is correct\n",
    "\n",
    "#A complete list of candidates who received votes\n",
    "candidates = election_df[\"Candidate\"].unique()\n",
    "print(candidates) #prints the complete list of candidates\n",
    "\n",
    "\n",
    "#The total number of votes each candidate won\n",
    "votes = election_df['Candidate'].value_counts() #shows the list of candidates and the number of votes each\n",
    "votes\n",
    "\n",
    "#The percentage of votes each candidate won\n",
    "type(votes)\n",
    "\n",
    "#The winner of the election based on popular vote\n",
    "most_votes = votes.max()\n",
    "#winner = min(candidates)\n",
    "winner = election_df['Candidate'].value_counts().nlargest(1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "8bd89c41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "------------------\n",
      "Total Votes 369711\n",
      "------------------\n",
      "Candidate\n",
      "Diana DeGette              272892\n",
      "Charles Casper Stockham     85213\n",
      "Raymon Anthony Doane        11606\n",
      "Name: count, dtype: int64\n",
      "------------------\n",
      "Winner:  Candidate\n",
      "Diana DeGette    272892\n",
      "Name: count, dtype: int64\n",
      "------------------\n"
     ]
    }
   ],
   "source": [
    "#OUPUT\n",
    "print(\"Election Results\")\n",
    "print(\"------------------\")\n",
    "print(f\"Total Votes\", total_votes_cast)\n",
    "print(\"------------------\")\n",
    "print(votes)\n",
    "print(\"------------------\")\n",
    "print(f\"Winner: \" , winner)\n",
    "print(\"------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "4bd518ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#WRITE TO TEXT FILE\n",
    "pyPoll = \"Resources/pyPoll.txt\"\n",
    "\n",
    "with open(\"pyPoll.txt\", mode=\"wt\") as f:  \n",
    "    f.write(\"Election Results\")\n",
    "    f.write(\"------------------\")\n",
    "    f.write(str(total_votes_cast))\n",
    "    f.write(\"------------------\")\n",
    "    f.write(str(votes))\n",
    "    f.write(\"------------------\")\n",
    "    f.write(f\"Winner: \")\n",
    "    f.write(str(winner))\n",
    "    f.write(\"------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0574c270",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
