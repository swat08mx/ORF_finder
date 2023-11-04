// code for driver main from py

public class DriverMain {
    public static void main(String[] args) {
        int count = 0;
        int result = 1;
        int number = 100;

        for (int f = 0; f < 3; f++) {
            String seqPos = getSequencePosition(f, result);

            if (count == 0) {
                System.out.println("The +" + (f + 1) + " reading frame is: " + seqPos + "\n");
            } else if (count == 1) {
                System.out.println("The -" + (f + 1) + " reading frame is: " + seqPos + "\n");
            }

            List<String> orfs = new ArrayList<>();
            int point = 0;
            boolean found = true;
            String finalString = "";

            for (int i = 0; i < seqPos.length(); i++) {
                try {
                    if (seqPos.charAt(i) == 'A' && seqPos.charAt(i + 1) == 'T' && seqPos.charAt(i + 2) == 'G') {
                        found = true;
                        for (int j = i + 3; j < seqPos.length(); j++) {
                            if (seqPos.charAt(j) == 'T' && seqPos.charAt(j + 1) == 'A' && seqPos.charAt(j + 2) == 'G') {
                                point++;
                                found = false;
                                break;
                            } else if (seqPos.charAt(j) == 'T' && seqPos.charAt(j + 1) == 'G' && seqPos.charAt(j + 2) == 'A') {
                                point++;
                                found = false;
                                break;
                            } else if (seqPos.charAt(j) == 'T' && seqPos.charAt(j + 1) == 'A' && seqPos.charAt(j + 2) == 'A') {
                                point++;
                                found = false;
                                break;
                            } else {
                                finalString += seqPos.charAt(j);
                            }
                        }
                        if (found) {
                            orfs.add("ATG" + finalString);
                            finalString = "";
                        }
                    }
                } catch (Exception e) {
                    // Ignore
                }
            }

            if (point != 0) {
                try {
                    for (int i = 0; i < orfs.size(); i++) {
                        String orf = orfs.get(i);
                        String newOrf = removeSpaces(orf);
                        if (newOrf.length() > number) {
                            if (point == 1) {
                                System.out.println("The ORFs " + (i + 1) + " is: " + orf + "TAG\n");
                            } else if (point == 2) {
                                System.out.println("The ORFs " + (i + 1) + " is: " + orf + "TGA\n");
                            } else if (point == 3) {
                                System.out.println("The ORFs " + (i + 1) + " is: " + orf + "TAA\n");
                            }
                            System.out.println("The amino acid sequence for ORF" + (i + 1) + " is: " + translate(orf) + "\n");
                        }
                    }
                } catch (Exception e) {
                    System.out.println("*******************There was an unknown error in translation at ORF, report this to dev.**********************\n");
                }
            } else {
                System.out.println("No reading frames were found\n");
            }

            if (!seqPos.contains("ATG")) {
                System.out.println("No reading frames were found\n");
