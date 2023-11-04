// code for dictionary 
public class Codons {
    public static final Map<String, String> CODONS = new HashMap<>();

    static {
        CODONS.put("GCT", "Ala");
        CODONS.put("GCC", "Ala");
        CODONS.put("GCA", "Ala");
        CODONS.put("GCG", "Ala");
        CODONS.put("CGT", "Arg");
        CODONS.put("CGC", "Arg");
        CODONS.put("CGA", "Arg");
        CODONS.put("CGG", "Arg");
        CODONS.put("AGA", "Arg");
        CODONS.put("AGG", "Arg");

        CODONS.put("AAT", "Asn");
        CODONS.put("AAC", "Asn");
        CODONS.put("GAT", "Asp");
        CODONS.put("GAC", "Asp");
        CODONS.put("TGT", "Cys");
        CODONS.put("TGC", "Cys");
        CODONS.put("CAA", "Gln");
        CODONS.put("CAG", "Gln");
        CODONS.put("GAA", "Glu");
        CODONS.put("GAG", "Glu");

        CODONS.put("GGT", "Gly");
        CODONS.put("GGC", "Gly");
        CODONS.put("GGA", "Gly");
        CODONS.put("GGG", "Gly");
        CODONS.put("CAT", "His");
        CODONS.put("CAC", "His");
        CODONS.put("ATT", "Ile");
        CODONS.put("ATC", "Ile");
        CODONS.put("ATA", "Ile");
        CODONS.put("TTA", "Leu");

        CODONS.put("TTG", "Leu");
        CODONS.put("CTT", "Leu");
        CODONS.put("CTC", "Leu");
        CODONS.put("CTA", "Leu");
        CODONS.put("CTG", "Leu");
        CODONS.put("AAA", "Lys");
        CODONS.put("AAG", "Lys");
        CODONS.put("ATG", "Met");
        CODONS.put("TTT", "Phe");
        CODONS.put("TTC", "Phe");

        CODONS.put("CCT", "Pro");
        CODONS.put("CCC", "Pro");
        CODONS.put("CCA", "Pro");
        CODONS.put("CCG", "Pro");
        CODONS.put("TCT", "Ser");
        CODONS.put("TCC", "Ser");
        CODONS.put("TCA", "Ser");
        CODONS.put("TCG", "Ser");
        CODONS.put("AGT", "Ser");
        CODONS.put("AGC", "Ser");

        CODONS.put("ACT", "Thr");
        CODONS.put("ACC", "Thr");
        CODONS.put("ACA", "Thr");
        CODONS.put("ACG", "Thr");
        CODONS.put("TGG", "Trp");
        CODONS.put("TAT", "Tyr");
        CODONS.put("TAC", "Tyr");
        CODONS.put("GTT", "Val");
        CODONS.put("GTC", "Val");
        CODONS.put("GTA", "Val");
        CODONS.put("GTG", "Val");
        CODONS.put("TAA", "");
        CODONS.put("TAG", "");
        CODONS.put("TGA", "");
    }

    // public static String translate(String codon) {
    //     return CODONS.get(codon);
    // }
}
 // code for reading file

 import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ReadSevenFasta {
    public static void main(String[] args) throws IOException {
        File file = new File("seven.fasta");
        FileReader reader = new FileReader(file);

        List<String> newlist = new ArrayList<>();
        String seq = "";
        for (String line : reader.lines().toList()) {
            if (line.contains("\n")) {
                newlist.add(line);
            }
        }

        for (int i = 1; i < newlist.size() - 1; i++) {
            seq += newlist.get(i);
        }

        String result = seq.lines().map(String::strip).collect(Collectors.joining());

        System.out.println(result);
    }
}




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
