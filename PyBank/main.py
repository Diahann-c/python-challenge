{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6e697f1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#IMPORT DEPENDANCIES\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f4725179",
   "metadata": {},
   "outputs": [],
   "source": [
    "#INSTRUCTIONS\n",
    "#The total number of months included in the dataset\n",
    "#The net total amount of \"Profit/Losses\" over the entire period\n",
    "#The changes in \"Profit/Losses\" over the entire period, and then the average of those changes\n",
    "#The greatest increase in profits (date and amount) over the entire period\n",
    "#The greatest decrease in profits (date and amount) over the entire period\n",
    "#Your analysis should align with the following results:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "215054a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#DECLARE VARIABLES\n",
    "total_months = 0\n",
    "amount = 0\n",
    "net_amount = 0\n",
    "changes_profit = 0\n",
    "avg_changes = 0\n",
    "greatest_increase = 0\n",
    "greatest_decrease = 0\n",
    "\n",
    "profit_losses=[] #creating a list to store profit/losses\n",
    "date = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c7c40bb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#READ CSV\n",
    "budget_data = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "34861a56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x0000016D476AEC80>\n",
      "CSV Header: ['Date', 'Profit/Losses']\n"
     ]
    }
   ],
   "source": [
    "with open (budget_data) as csvfile: #need to read the csv file\n",
    "    csvreader = csv.reader(csvfile, delimiter = ',')\n",
    "    print(csvreader)\n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\") #prints out headers\n",
    "    \n",
    "    for row in csvreader:\n",
    "        #print(row) #just wanted to verify that the entire data set was being read\n",
    "        \n",
    "        #The total number of months included in the dataset\n",
    "        total_months = total_months + 1\n",
    "        date.append(row[1])\n",
    "        \n",
    "        #The net total amount of \"Profit/Losses\" over the entire period\n",
    "        amount = int(row[1])\n",
    "        net_amount += amount\n",
    "        \n",
    "        #The changes in \"Profit/Losses\" over the entire period, and then the average of those changes\n",
    "        profit_losses.append(row)\n",
    "        avg_changes = (net_amount/total_months)\n",
    "        \n",
    "        #The greatest increase in profits (date and amount) over the entire period\n",
    "        greatest_increase = max(profit_losses)\n",
    "        \n",
    "        #The greatest decrease in profits (date and amount) over the entire period\n",
    "        greatest_decrease = min(profit_losses)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b1404f19",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months:602\n",
      "Total: $157949386\n",
      "Average Change:262374.3953488372\n",
      "Greatest Increase in Profits:['Sep-16', '898241']\n",
      "Greatest Decrease in Profits:['Apr-10', '-728133']\n"
     ]
    }
   ],
   "source": [
    "#Your analysis should align with the following results:\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "print(\"Total Months:\" + str(total_months))\n",
    "print(\"Total: $\" + str(net_amount))\n",
    "print(\"Average Change:\" + str(avg_changes))\n",
    "print(\"Greatest Increase in Profits:\" + str(greatest_increase))\n",
    "print(\"Greatest Decrease in Profits:\" + str(greatest_decrease))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c7307060",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create Text File with Results\n",
    "# Print the results to \"PyBank.txt\" file\n",
    "print(\"Financial Analysis\", file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"----------------------------\", file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"Total Months:\" + str(total_months), file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"Total: $\" + str(net_amount), file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"Average Change:\" + str(avg_changes), file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"Greatest Increase in Profits:\" + str(greatest_increase), file=open(\"PyPoll.txt\", \"a\"))\n",
    "print(\"Greatest Decrease in Profits:\" + str(greatest_decrease), file=open(\"PyPoll.txt\", \"a\"))\n"
   ]
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
