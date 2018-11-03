import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Scanner;

public class HashBrute extends JFrame {

	private JTextField hashField;
	private JTextField resultField;
	private JComboBox comboBox1;

	ArrayList<String> passwords = new ArrayList<>();
	File passwordsFile = null;

	public HashBrute() throws HeadlessException {
		super("Hash brute by stdian");
		createGUI();
	}

	public void createGUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setResizable(false);

		JPanel panel = new JPanel();
		panel.setLayout(new FlowLayout());

		JLabel hashLabel = new JLabel("Hash:  ");
		panel.add(hashLabel);

		hashField = new JTextField();
		hashField.setColumns(32);
		panel.add(hashField);

		JLabel resultLabel = new JLabel("Result:");
		panel.add(resultLabel);

		resultField = new JTextField();
		resultField.setColumns(32);
		resultField.setEditable(false);
		panel.add(resultField);

		comboBox1 = new JComboBox();
		comboBox1.addItem("MD5");
		comboBox1.addItem("SHA-1");
		comboBox1.addItem("SHA-256");
		panel.add(comboBox1);

		JButton button2 = new JButton("Open dictionary");
		panel.add(button2);

		JButton button1 = new JButton("Brute");
		panel.add(button1);

		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (passwordsFile == null) {
					JOptionPane.showMessageDialog(null, "First open dictionary");
				}
				else if (hashField.getText().trim().equals("")) {
					JOptionPane.showMessageDialog(null, "First input hash");
				} else {
					button1.setEnabled(false);
					String result = null;
					try {
						result = brute(hashField.getText().trim(), (String) comboBox1.getSelectedItem());
					} catch (Exception ex) {

					}
					resultField.setText(result);
					button1.setEnabled(true);
				}
			}
		});

		button2.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				JFileChooser fileopen = new JFileChooser();
				int ret = fileopen.showDialog(null, "Открыть файл");
				if (ret == JFileChooser.APPROVE_OPTION) {
					File file = fileopen.getSelectedFile();
					try {
						Scanner sc = new Scanner(file);

						try {
							if (sc.hasNextLine()) {
								String pass = sc.nextLine();
								passwordsFile = file;
							}
						} catch (Exception e2) {
							JOptionPane.showMessageDialog(null, "Error reading file!");
						}
					} catch (FileNotFoundException e1) {
						JOptionPane.showMessageDialog(null, "File not found!");
					}

				}
			}
		});

		getContentPane().add(panel);
		setPreferredSize(new Dimension(350, 150));
	}


	public static void main(String[] args) {

		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch (Exception ex) {}

		javax.swing.SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				JFrame.setDefaultLookAndFeelDecorated(true);
				HashBrute frame = new HashBrute();
				frame.pack();
				frame.setLocationRelativeTo(null);
				frame.setVisible(true);
			}
		});
	}

	String brute(String hash, String type) throws NoSuchAlgorithmException, IOException {

		Scanner sc = new Scanner(passwordsFile);

		if (type.equals("MD5")) {
			MessageDigest m = MessageDigest.getInstance("MD5");
			m.reset();

			while (sc.hasNextLine()) {
				String pass = sc.nextLine();
				pass = pass.trim();
				if (!pass.equals("")) {
					m.update(pass.getBytes("utf-8"));
					String s2 = new BigInteger(1,m.digest()).toString(16);
					while(s2.length() < 32 ){
						s2 = "0" + s2;
					}
					if (hash.equals(s2)) {
						return pass;
					}
				}
			}

		}

		return "Password not found";
	}

}
